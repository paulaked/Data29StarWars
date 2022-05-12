import pymongo
import requests
import json


#connecting and using starwars database on Mongodb:
client = pymongo.MongoClient()
db = client["starwars"]

db.drop_collection("starships")




starships_req = requests.get("https://swapi.tech/api/starships")