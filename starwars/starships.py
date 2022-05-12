import starwars.app.requesting_sw as rq
import json
import requests
import pymongo

client = pymongo.MongoClient()
db = client['starwars']


class Starships:

    # Class attributes
    def __init__(self):
        self.content = {}
        self.starships = {}
        self.ship_info = []

    # Requesting data from api using request import
    # Converts bjson to json, stores as dictionary
    def requesting(self):
        try:
            self.content = json.loads(rq.sw.content)
            print("Code 200: request successful")
            next_page = self.content['next']
            self.get_next_page(next_page)
        except:
            raise
        finally:
            print("Requests Executed")

        return self.content

    # Method to retrieve starship page data from each valid page
    def get_next_page(self, next_page):
        while next_page:
            page_content = self.get_url(next_page)
            self.content['results'].extend(page_content['results'])
            next_page = page_content['next']
        return next_page

    # Method to retrieve starship info
    def get_starships(self):
        try:
            self.starships = self.content["results"]
            print("Starships Retrieved")
        except:
            raise
        finally:
            print("Get starships method executed")
        return self.starships

    # Method to retrieve any content from a given URL in json
    def get_url(self, url):
        return json.loads(requests.get(url).content)

    # Method to retrieve information for each ship from their URLS
    def get_ship_info(self):
        ships = []
        for ship in self.starships:
            ships.append(self.get_url(ship["url"]))
        for ship in ships:
            self.ship_info.append(ship["result"]["properties"])
        return self.ship_info

    # Sets pilot names to None - Subroutine in get_pilot_info
    def empty_pilots(self, ship):
        ship["pilots"] = None
        return ship

    # Sets pilot names to names given in each URL - Subroutine in get_pilot_info
    def pilots_exist(self, ship):
        pilots = []
        for url in ship["pilots"]:
            pilots.append(self.get_url(url)["result"]["properties"]["name"])
        ship.update({"pilots": pilots})
        print("Starship: " + ship["name"] + " has pilots: ", ship["pilots"])
        return ship

    # Method to set pilot names accordingly
    def get_pilot_info(self):
        for ship in self.ship_info:
            if not ship["pilots"]:
                self.empty_pilots(ship)
            else:
                self.pilots_exist(ship)
        return self.ship_info

    # Creates empty collection for starships unless it exist
    def create_collection(self):
        if 'starships' in db.list_collection_names():
            print("starships: This colection already exists.")
            return
        else:
            print("starships: Colection has been added.")
            return (db.create_collection('starships'))

    # Creates document for each starship
    def add_starships_docs(self):
        for ship in self.ship_info:
            db.starships.insert_one(ship)
            print(ship['name'], ": added to collection")
        return db.starships.find({})

    # Replaces pilot name(s) with Character IDs for each starship
    def id_replace(self):
        for ship in self.ship_info:
            if ship['pilots'] != None:
                id_list = []
                for name in ship['pilots']:
                    ob = db.characters.find({'name': name}, {'_id': 1})
                    for id in ob:
                        id_list.append(id)
                db.starships.update_one({'pilots': ship['pilots']},
                                        {'$set': {'pilots': id_list}})
                print(ship['pilots'], ': has been replaced with: ', id_list)
        return db.starships.find({})
