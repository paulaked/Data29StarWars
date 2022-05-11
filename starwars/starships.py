import starwars.app.requesting_sw as rq
import json
import requests


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
        except:
            raise
        finally:
            print("Requests Executed")

        return self.content

    # Method to retrieve starship info
    def get_starships(self):
        try:
            self.starships = self.content["results"]
            print("Starships Retrieved")
        except:
            raise
        finally:
            print("Starships method executed")
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

    # Sets pilot names to None
    def empty_pilots(self, ship):
        ship["pilots"] = None
        return ship

    # Sets pilot names to names given in each URL
    def pilots_exist(self, ship):
        pilots = []
        for url in ship["pilots"]:
            pilots.append(self.get_url(url)["result"]["properties"]["name"])
        ship.update({"pilots": pilots})
        print("Starship " + ship["name"] + " has pilots: " + ship["pilots"])
        return ship

    # Method to set pilot names accordingly
    def get_pilot_info(self):
        for ship in self.ship_info:
            if not ship["pilots"]:
                self.empty_pilots(ship)
            else:
                self.pilots_exist(ship)
        return self.ship_info
