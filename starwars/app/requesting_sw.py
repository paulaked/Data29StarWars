# Step 1 - Import necessary python packages:
import requests
import pymongo
import json

# Step 2 - Connecting and using starwars database on Mongodb:
client = pymongo.MongoClient()
db = client['starwars']

web_address = 'https://www.swapi.tech/api/starships'


# Step 3 - This function extracts the data from the corresponding API:
def extract_data(url):
    starship_url = requests.get(url)
    starship_url = starship_url.json()
    return starship_url

# Step 4 - The first page of the URL is stored as a list:
starship_page = [value['url'] for value in extract_data(web_address)['results']]


# Step 5 - This function extracts the starship's URLs for the remaining pages and adds them to the previous list:
def get_url_for_all_pages():
    current_page = extract_data(web_address)
    while current_page['next'] != None:
        current_page = requests.get(current_page['next'])
        current_page = current_page.json()
        for item in current_page['results']:
            starship_page.append(item['url'])
    return starship_page


# Step 6 - The last function extracts the name of the pilots to find their ID and replace the URL with the ID:
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
            pilot_content = requests.get(pilot)
            pilot_content = pilot_content.json()
            pilot_name.append(pilot_content['result']['properties']['name'])
        pilots_id = []
        for i in pilot_name:
            for n in db.characters.find({'name': i}):
                pilots_id.append(n["_id"])
        url_content['result']['properties']['pilots'] = pilots_id
        starships.append(url_content)
    return starships


# Step 7 - Drop the existing starship collection from Mongodb then create a new collection:
db.drop_collection("Starship")
print('dropped')

db.create_collection("Starship")
print('the collection was created successfully')

# Step 8 - All starships are added to the Starship collection on Mongodb:
for i in get_and_replace_pilots_id():
    db.Starship.insert_one(i)

print("The starships have been added successfully")

