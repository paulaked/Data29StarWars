import requests
import json

# get starships data
# - make request for starships
# - input - none
# - outpu
# t - dict


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
        return print(self.starships_data)

some_data = StarshipsData()

# data.get_raw_starship_data()
# data.starships_url_list()
# data.get_starships_data()

# print(data.data)
# print(data.url_list)
# print(data.starships_data)
some_data.get()

# check data is ready for insert
# - check certain keys exists


def data_ready(data):
    pass


# put data into a collection
# - create collection
# - use insert_many
# - input - dict
# - output - collection


def insert_starships(data):
    pass