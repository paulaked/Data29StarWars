import requests
import json
import pymongo

# i need to replace pilot urls with character object ids
# i need a link between pilot urls and character object ids
# - i can query pilot url for character name and link with character name in document

# parent - for each starship in the collection
# overarching def, will hold child def(s) inside
# - (child) for each pilot url
# - query the url for person
# - (child) for each person name
# - match with name on characters collection
# - (child) replace url with character object id


class ReplacePilots():

    client = pymongo.MongoClient()
    db = client["starwars"]

    def __init__(self):
        self.pilot_url_list = []

    # child - get pilot list, (pilot list might be empty)
    # - input is document from the starships collection
    # - output will be the pilot url list (if exists)

    def get_pilot_url_list(self):
        self.pilot_url_list = db.starships.find()
        return self.pilot_url_list


attempt = ReplacePilots()
print(attempt.pilot_url_list)


# print(the_collection.get())

# child - perform query on pilot url
# - input will be pilot url
# - output will be the pilot name (people name)

# child - find match of pilot name from characters collection
# - do a find on the characters collection based on the pilot name
# - return object id for character

# child - update the pilot field in starships collection

# - iterate through pilot list
# -- each item in pilot list is a url
# -- so i will need to get a response from each url
# -- if the