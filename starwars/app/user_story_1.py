import requests
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

# class to get starships data and put into a collection


class StarshipsData:

    def __init__(self):
        self.data = []
        self.url_list = []
        self.starships_data = []

    # method to retrieve raw data from api and return in dict type, stored as class attribute
    def get_raw_starship_data(self):
        try:
            for i in list(range(1,5)):
                for item in requests.get(f"https://www.swapi.tech/api/starships?page={i}&limit=10").json()["results"]:
                    self.data.append(item)
            return self.data
        except:
            print("an error happened")

    # method to extract the urls from the raw api response and append to list and store as class attribute
    def starships_url_list(self):
        for starship in self.data:
            self.url_list.append(starship["url"])
        return self.url_list

    # method to query each starship url and append response in dict form to list and store as class attribute
    def get_starships_data(self):
        placeholder_list = []
        for url in self.url_list:
            placeholder_list.append(requests.get(url).json()["result"])
        self.starships_data = placeholder_list
        return self.starships_data

    # method which calls on all class methods and creates and inserts starships data to collection for use
    def create_collection(self):
        self.get_raw_starship_data()
        self.starships_url_list()
        self.get_starships_data()
        db.create_collection("starships")
        db.starships.insert_many(self.starships_data)