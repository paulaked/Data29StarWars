import requesting_sw
import pymongo
import json
import requests

client = pymongo.MongoClient()
db = client["starwars"]

#db.drop_collection("starships")

starships_req = requests.get("https://www.swapi.tech/api/starships")
characters_req = requests.get("https://www.swapi.tech/api/people")


starships_req_json = starships_req.json()

characters_req_json = characters_req.json()


#print(starships_req_json["results"])

#for i in starships_req_json['results']:
#    print(i['url'])


for i in starships_req_json['results']:
    print(requests.get(i['url']).json())

#for i in characters_req_json['results']:
#    print(requests.get(i['_id']).json())

# not urls, object ids of database

#temp_ships = []
#temp_pilots = []
#x = starships_req_json["result"]["properties"]["name"]
#pilots = starships_req_json["result"]["properties"]["pilots"]
#if pilots != 0:
#    for i in range(0,len(pilot)):
#        temp_ships.append(x)
#        temp_pilots.append(pilots[i])
#else:
#    print(x + "no pilot")
