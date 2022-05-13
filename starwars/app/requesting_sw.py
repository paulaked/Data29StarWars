import pymongo
import starwars.config_manager as conf
import requests
import json

client = pymongo.MongoClient()
db = client["starwars"]

sw = requests.get("https://www.swapi.tech/api/starships") # imports data from the first page of the api
sw_1 = sw.json()

# The function below extracts all the data from all four pages.


def get_starships(sw_1): # gets the raw data
    url = sw_1['next'] # filters the data so that the next page can be extracted
    while url != None:
        print(url)
        content = requests.get(url).json() # gets the data from all four pages.
        starship = content['results']
        sw_1['results'].extend(starship) # this merges all the data pages into one
        url = content['next']
    return sw_1


print(get_starships(sw_1))


starships_1 = []
for i in sw_1['results']: # filters the data to display on the results key
    x = requests.get(i['url']).json()
    pilot = x['result']['properties'] # filters the data to display on the results key
    starships_1.append(pilot)
print(starships_1)

# Replaces pilots urls to names and then to object id


for i in starships_1:
    x = requests.get(i['url']).json()
    pilot = x['result']['properties']['pilots']  # filters the data to get pilot information
    if len(pilot) >= 1:  # filters out all the empty pilot fields
        new_pilot = pilot
        pilots = []
        for n in new_pilot:

            w = requests.get(n).json() # pulls out
            update_pilot = w['result']['properties']['name']  # filters the names of the pilots
            pilots.append(db.characters.find_one({"name": update_pilot}, {"_id": 1}))  # appends the pilots names
            # with a list of ObjectIDs
        i["pilots"] = pilots

print(starships_1)

# adds to MongoDB
db.drop.collection('starships')
db.create_collection("starships")
db.starships.insert_many(starships_1)