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

    def get_starships(self):
        try:
            self.starships = self.content["results"]
            print("Starships Retrieved")
        except:
            raise
        finally:
            print("Starships method executed")
        return self.starships

    def get_url(self,url):
        return json.loads(requests.get(url).content)

    def get_ship_info(self):
        ships = []
        for ship in self.starships:
            ships.append(self.get_url(ship["url"]))
        for ship in ships:
            self.ship_info.append(ship["result"]["properties"])

    def get_pilot_info(self):
        for ship in self.ship_info:
            if ship["pilots"] == []:
                self.ship_info["pilots"] = None
            else:
                pilots =[]
                for url in ship["pilots"]:
                    pilots.append(self.get_url(url)["result"]["properties"]["name"])





