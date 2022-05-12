import starwars.config_manager as conf
import requests

sw = requests.get("https://www.swapi.tech/api/starships/9")

def total_valid(url):
    valid = []
    sw = requests.get(url).json()
    total = sw["total_records"]
    for i in range(1, total + 1):
        sws = requests.get(url+str(i))
        if sws.status_code != 404:
            valid.append(i)
    return valid
print (total_valid("https://www.swapi.tech/api/starships"))


def no_pilots(ships, url):
    no_pilots = []
    for i in ships:
        sw = requests.get(url+str(i))
        data = sw.json()
        ship_name = data["result"]["properties"]["name"]
        pilot = data["result"]["properties"]["pilots"]
        if len(pilot) <= 0:
            no_pilots.append(ship_name)
    return no_pilots

def star_ships(ships, url):
    ships_pilot = {}
    for i in ships:
        temp = []
        sw = requests.get(url+str(i))
        data = sw.json()
        ship_name = data["result"]["properties"]["name"]
        pilot = data["result"]["properties"]["pilots"]
        if len(pilot) > 0:
            for num in range(0, len(pilot)):
                temp.append(pilot[num])
            ships_pilot[ship_name] = temp
    return ships_pilot
