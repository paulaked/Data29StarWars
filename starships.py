import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

db.drop_collection("starships")

