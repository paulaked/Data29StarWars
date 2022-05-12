import pymongo
import starwars.config_manager as conf
import requests


sw = requests.get("https://www.swapi.tech/api/starships/")
client = pymongo.MongoClient()
db = client["starwars"]

pilot_vehicle = {}

def starships(vehicle):
    temp_vehicle = []
    temp_pilot = []
    pilot_vehicle = {}

    for i in vehicle:
        sw = requests.get("https://www.swapi.tech/api/starships/"+str(i))
        data = sw.json()
        h = data["result"]["properties"]["name"]
        pilot = data["result"]["properties"]["pilots"]
        if len(pilot) <= 0:
            for i in range(0, len(pilot)):
                pilot_vehicle[h] = i

                temp_vehicle.append(h)
                temp_pilot.append(pilot[i])

        else:
            print(h + " no pilot")

    print(temp_vehicle)
    print(temp_pilot)
    print(pilot_vehicle)

print(sw)