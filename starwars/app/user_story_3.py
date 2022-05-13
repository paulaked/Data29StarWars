import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

# replace pilot names with object ids

# function which queries the starships collection for all documents and return list of dicts
def list_starship():
    all_starships = db.starships.find()
    list_starships = []
    for starship in all_starships:
        list_starships.append(starship)
    return list_starships

# function to replace names with related objectIDs (works similar to replace_urls in user_story2)
def replace_names():
    for starship in list_starship():
        if starship["properties"]["pilots"] == []:
            pass
        else:
            print(starship["properties"]["model"])
            object_id_list = []
            for name in starship["properties"]["pilots"]:
                # query the characters database to get the object id based on the name
                object_id = db.characters.find_one({"name":name}, {"_id":1})["_id"]
                object_id_list.append(object_id)
                print(object_id)
            # update the starships collection by replacing names with object IDs
            db.starships.update_one({"_id": starship["_id"]}, {"$set": {"properties.pilots": object_id_list}})