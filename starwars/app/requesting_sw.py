import json
import starwars.config_manager as conf
import requests
import pymongo


client = pymongo.MongoClient()
db = client["starwars"]

# requesting data from api and turning into json files
def get_api(url):
    starship_req = requests.get(url)
    return starship_req

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
            #pilot_id = db.characters.find_one({"name": }, {"_id":1})
            #properties['new pilots'].append(pilot_id)
            #id = db.characters.find_one({"name":properties['new pilots']}, {"_id": 1})
    print(properties)
    if properties['new pilots'] != []:
        for pilot in properties['new pilots']:
            pilot_id = db.characters.find_one({"name":pilot}, {"_id":1})
            properties['new pilots'].append(pilot_id)
    print(properties)


pilot_list = []
#for pilot in properties['pilots']:
 #   print(pilot)
    #pilot_name =(requests.get(character).json()['result']['properties']['name'])
  #  pilot_id = db.characters.find_one({"name":pilot}, {"_id":1})
   # print(pilot_id)
    #pilot_list.append(pilot_id)
    #print(pilot_list)
#print(pilot_list)






#changing name to character id




































