import json
import starwars.config_manager as conf
import requests
import pymongo


client = pymongo.MongoClient()
db = client["starwars"]

# requesting data from api and turning into json files
starship_req = requests.get("https://swapi.tech/api/starships").json()
starship_req2 = requests.get("https://www.swapi.tech/api/starships?page=2&limit=10").json()
starship_req3 = requests.get("https://www.swapi.tech/api/starships?page=3&limit=10").json()
starship_req4 = requests.get("https://swapi.tech/api/starships?page=4&limit=10").json()

#getting results
list = starship_req.get('results')
list2 = starship_req2.get('results')
list3 = starship_req3.get('results')
list4 = starship_req4.get('results')

#getting the urls for all the starships into one list
starship_urls = []
for i in list:
    starship_urls.append(i.get('url'))
for i in list2:
    starship_urls.append(i.get('url'))
for i in list3:
    starship_urls.append(i.get('url'))
for i in list4:
    starship_urls.append(i.get('url'))
#print(starship_urls)

#getting properties for all the starships and changing the pilot urls to pilot names
for url in starship_urls:
    properties = requests.get(url).json()['result']['properties']
    properties['new pilots'] = []
    if properties['pilots'] == []:
        pass
    else:
        for character in properties['pilots']:
            properties['new pilots'].append(requests.get(character).json()['result']['properties']['name'])
    print(properties)
    place_holder_list = []
    if properties['new pilots'] != []:
        for pilot in properties['new pilots']:
            pilot_id = db.characters.find_one({"name":pilot}, {"_id":1})
            place_holder_list.append(pilot_id)
        print(place_holder_list)
        properties['new pilots'] = place_holder_list
        print(properties)

#drop existing starships collection on Mongodb
db.drop_collection("starships")
#create starships collection on Mongodb assuming it doesnt already exist
db.create_collection("starships")

#adding the starships to the starship collection on Mongodb by iterating through each starship
def add_to_mongodb():
    for i in get_properties_name_characterID():
       db.starships.insert_one(i)






































