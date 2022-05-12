import pymongo
import requests
import json
import starwars.app.requesting_sw as r_q

client = pymongo.MongoClient()
db = client["starwars"]

db.drop_collection("starships")


class Starships:
    def __init__(self):
        self.ship_info = []
        self.content = {}
        self.star_ship = {}

