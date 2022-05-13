import requests
import pymongo

# create starships collection and insert starships to collection

def replace_names():
    for starship in list_starship():
        if starship["properties"]["pilots"] == []:
            pass
        else:
            print(starship["properties"]["model"])
            pilot_names = []
            for pilot_url in starship["properties"]["pilots"]:
                name = requests.get(pilot_url).json()["result"]["properties"]["name"]
                pilot_names.append(name)
            db.starships.update_one({"_id": starship["_id"]}, {"$set": {"properties.pilots": f"{pilot_names}"}})
    pass