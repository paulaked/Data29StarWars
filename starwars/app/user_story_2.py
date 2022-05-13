import requests
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]


def list_starship():
    all_starships = db.starships.find()
    list_starships = []
    for starship in all_starships:
        list_starships.append(starship)
    return list_starships


def replace_urls():
    for starship in list_starship():
        if starship["properties"]["pilots"] == []:
            pass
        else:
            # print(starship["properties"]["model"])
            pilot_names = []
            for pilot_url in starship["properties"]["pilots"]:
                name = requests.get(pilot_url).json()["result"]["properties"]["name"]
                pilot_names.append(name)
            db.starships.update_one({"_id": starship["_id"] }, {"$set": {"properties.pilots": pilot_names }})


replace_urls()
