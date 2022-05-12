import requests
import json
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

# get starships data
# - make request for starships
# - input - none
# - output - dict


class StarshipsData:

    def __init__(self):
        self.data = []
        self.url_list = []
        self.starships_data = []

    def get_raw_starship_data(self):
        try:
            raw_data = requests.get("https://swapi.tech/api/starships").json()["results"]
            self.data = raw_data
        except:
            print("an error happened")
        return self.data

    def starships_url_list(self):
        for starship in self.data:
            self.url_list.append(starship["url"])
        return self.url_list

    def get_starships_data(self):
        placeholder_list = []
        for url in self.url_list:
            placeholder_list.append(requests.get(url).json()["result"])
        self.starships_data = placeholder_list
        return self.starships_data

    def get(self):
        self.get_raw_starship_data()
        self.starships_url_list()
        self.get_starships_data()

    def insert_to_new_collection(self):
        db.create_collection("starships")
        db.starships.insert_many(self.starships_data)

# some_data = StarshipsData()
# some_data.get()
# some_data.insert_to_collection()
