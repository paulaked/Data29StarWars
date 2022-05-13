import requests
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

# get starships data and put into a collection


class StarshipsData:

    def __init__(self):
        self.data = []
        self.url_list = []
        self.starships_data = []

    def get_raw_starship_data(self):
        try:
            for i in list(range(1,5)):
                for item in requests.get(f"https://www.swapi.tech/api/starships?page={i}&limit=10").json()["results"]:
                    self.data.append(item)
            return self.data
        except:
            print("an error happened")

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

    def create_collection(self):
        self.get_raw_starship_data()
        self.starships_url_list()
        self.get_starships_data()
        db.create_collection("starships")
        db.starships.insert_many(self.starships_data)


# some_data = StarshipsData()
# some_data.create_collection()