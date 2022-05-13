import requests
import pymongo
import json

#Access to database 
client = pymongo.MongoClient()
db = client['starwars']

#Created a function to EXTRACT data from API link
web_address = 'https://www.swapi.tech/api/starships'
def data(url_address):
    ship_url = requests.get(url_address)
    ship_url = ship_url.json() #converted to a JSON file
    return ship_url
starship_page = [value['url'] for value in data(web_address)['results']] #Extracted all the URL's from the first page

#MORE EXCTRACTION : Function to get all the remaining URL's from the different pages
def get_url_data_from_all_pages():
    page_1 = data(web_address)
    while page_1['next'] != None: # ensuring that the pages i extract give me pages that have data so i ensure that data is not eaual to none
        page_1 = requests.get(page_1['next'])
        page_1 = page_1.json() #coverted to a JSON file
        for item in page_1['results']:
            starship_page.append(item['url'])
    return starship_page

# EXTRACTED all the pilot names and match their id on character collection. Replace values
def get_and_replace_pilots_id():
    starships = [] 
    for i in get_and_replace_pilots_id():
        url_info = requests.get(i)
        url_info = url_info.json()
        result = url_info['result']
        properties = result['properties']
        pilot_url = properties['pilots']
        pilot_name = [] # Pilot empty list name created

        #created a for loop requesting the pilot name and details from their url to add to list created
        for pilot in pilot_url:
            pilot_info = requests.get(pilot)
            pilot_info = pilot_info.json()
            pilot_name.append(pilot_info['result']['properties']['name']) #add all the result properties and name in to the pilot name created
        
        # Creating an empty list to replace the pilot with ID.
        pilots_id = []
        for i in pilot_name:
            for info in db.characters.find({'name': i}):
                pilots_id.append(info["_id"])
        url_info['result']['properties']['pilots'] = pilots_id

        starships.append(url_info)

    return starships

# Drop starship collection from MongoDB and uploadind into collection
# More starships added on Mongodb:
db.drop_collection("Starship")
print('dropped')
db.create_collection("Starship")
print('Successful Creation')
for i in get_and_replace_pilots_id():
    db.Starship.insert_one(i)

