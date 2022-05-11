import pymongo
import requests
import json

client = pymongo.MongoClient()
db = client["starwars"]

starships_req = requests.get("https://swapi.tech/api/starships")

starships_json = starships_req.json()

with open("starwars", "w") as jsonfile:
    json.dump(starships_json, jsonfile)
