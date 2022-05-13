import requests
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

# replace pilot urls with pilot names


# function to query mongodb starships collection for all objects and return as list of dicts for use
def list_starship():
    all_starships = db.starships.find()
    list_starships = []
    for starship in all_starships:
        list_starships.append(starship)
    return list_starships


# function which replaces urls of pilots with names of pilots
def replace_urls():
    # looping through list of dict
    for starship in list_starship():
        # do nothing if the pilots value is empty
        if starship["properties"]["pilots"] == []:
            pass
        else:
            # a placeholder list to hold names (when there is more than one pilot) and loop through them
            pilot_names = []
            for pilot_url in starship["properties"]["pilots"]:
                # query the url to get the name and store the name
                name = requests.get(pilot_url).json()["result"]["properties"]["name"]
                # add this name to the placehold list
                pilot_names.append(name)
            # update the relevant document with the list of names
            db.starships.update_one({"_id": starship["_id"] }, {"$set": {"properties.pilots": pilot_names }})