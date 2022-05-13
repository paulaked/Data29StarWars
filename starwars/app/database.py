
import pymongo
# Connects to the 'starwars' database
client = pymongo.MongoClient()
db = client["starwars"]


# This function creates a 'starships' collection if there isn't one in the database.
# If there is one already present it drops it and creates a new one.
def creating_starships():

    if "starships" in db.list_collection_names():
        db.drop_collection("starships")
        db.create_collection("starships")
    else:
        db.create_collection("starships")

# This function adds the ships to the 'starships' collection
# If the ship has a pilot it replaces the name with the id from the 'characters' collection
def add_ships_data(data):
    for i in data:
        pilot_id = []
        # If the ship has pilots
        if len(i["pilots"])>0:
            for x in i["pilots"]:
                id=db.characters.find_one({"name": x}, {"_id": 1})
                pilot_id.append(id)
                # Finds the id of the pilots and adds it to a list
            db.starships.insert_one({
                "name": i["name"],
                "model": i["model"],
                "manufacturer": i["manufacturer"],
                "length": i["length"],
                "cost_in_credits": i["cost_in_credits"],
                "hyperdrive_rating": i["hyperdrive_rating"],
                "max_atmosphering_speed": i["max_atmosphering_speed"],
                "crew": i["crew"],
                "passengers": i["passengers"],
                "pilot": pilot_id

            })
        else:
            # Adds the ships with no pilots to the 'starship' collection
            db.starships.insert_one({
                "name": i["name"],
                "model": i["model"],
                "manufacturer": i["manufacturer"],
                "length": i["length"],
                "cost_in_credits": i["cost_in_credits"],
                "hyperdrive_rating": i["hyperdrive_rating"],
                "max_atmosphering_speed": i["max_atmosphering_speed"],
                "crew": i["crew"],
                "passengers": i["passengers"],
                "pilot": db.characters.find_one({"name": i["pilots"]}, {"_id": 1})

            })


























# creating_starships()
#
# db.starships.insert_one()
#
#
#
# #print(db.characters.find_one({"name": "Darth Vader"}, {"_id": 1, "name": 1}))
#
# db.starships.insert_one({
#   "name": "TIE Advanced x1",
#   "model": "Twin Ion Engine Advanced x1",
#   "manufacturer": "Sienar Fleet Systems",
#   "length": 9.2,
#   "max_atmosphering_speed": 1200,
#   "crew": 1,
#   "passengers": 0,
#   "pilot": db.characters.find_one({"name": "Darth Vader"}, {"_id": 1})
# })