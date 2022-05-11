import requesting_sw
import pymongo
import json
import requests

client = pymongo.MongoClient()
db = client["starwars"]

#db.drop_collection("starships")

starships_req = requests.get('https://www.swapi.tech/api/starships%27')


