import requests
import pymongo

# replace pilot names with object ids

client = pymongo.MongoClient()
db = client["starwars"]


def list_starship():
    all_starships = db.starships.find()
    list_starships = []
    for starship in all_starships:
        list_starships.append(starship)
    return list_starships


def replace_names():
    for starship in list_starship():
        if starship["properties"]["pilots"] == []:
            pass
        else:
            print(starship["properties"]["model"])
            object_id_list = []
            for name in starship["properties"]["pilots"]:
                print(name)
                object_id = db.characters.find_one({"name":name}, {"_id":1})["_id"]
                object_id_list.append(object_id)
                print(object_id)
            db.starships.update_one({"_id": starship["_id"]}, {"$set": {"properties.pilots": object_id_list}})

# list_starship()
# replace_names()

# print(db.characters.find_one({"name": "Darth Vader"},{"_id":1}))
# print(db.characters.find_one({"name": "Darth Vader"},{"_id":1})["_id"])