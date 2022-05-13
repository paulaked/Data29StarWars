#import libraries
import requests
import pymongo


client = pymongo.MongoClient()
db = client['starwars']


starships_address = 'https://www.swapi.tech/api/starships'

def get_data(url):
    starship_url = requests.get(url)
    starship_url = starship_url.json()
    return starship_url

starship_url_pages = []
for value in get_data(starships_address)['results']:
    starship_url_pages.append(value['url'])


#starship_url_pages = [value['url'] for value in get_data(starships_address)['results']]



def get_url_for_all_pages():
    current_page = get_data(starships_address)
    while current_page['next'] != None:
        current_page = requests.get(current_page['next'])
        current_page = current_page.json()
        for item in current_page['results']:
            starship_url_pages.append(item['url'])
    return starship_url_pages

def get_and_replace_pilots_id():
    starships = []
    for i in get_url_for_all_pages():
        url_content = requests.get(i)
        url_content = url_content.json()
        result = url_content['result']
        properties = result['properties']
        pilot_url = properties['pilots']
        pilot_name = []
        for pilot in pilot_url:
            pilot_content = requests.get(pilot).json()
            #pilot_content = pilot_content.json()
            pilot_name.append(pilot_content['result']['properties']['name'])
        pilots_id = []
        for i in pilot_name:
            for n in db.characters.find({'name': i}):
                pilots_id.append(n["_id"])
        url_content['result']['properties']['pilots'] = pilots_id
        starships.append(url_content)

    return starships

# 7. Drops the existing collection called Starship from the Mongo Database:
db.drop_collection("Starship")
print('Starship Collection has been dropped from the Mongo Database')

# 8. Creating a collection called Starship if non-existent on the Mongo Database:
db.create_collection("Starship")
print('The Starship collection has been created')

# 9. For loop to insert Starships into the collection on Mongo database:
for i in get_and_replace_pilots_id():
    db.Starship.insert_one(i)
print("The Starships have been added to the collection")



