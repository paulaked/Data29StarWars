import starwars.app.requesting_sw as rq
import json
import requests
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

#db.drop_collection("starships")


class Starships:

    # Class attributes
    def __init__(self):
        self.ship_info = []
        self.content = {}
        self.starships = {}
