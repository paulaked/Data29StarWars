import starwars.config_manager as conf
import requests
import json

sw = requests.get("https://www.swapi.tech/api/starships")

sw_1 = sw.json()

for i in sw_1['results']:
    x = requests.get(i['url']).json()
    pilot = x['result']
    print(pilot)

for i in sw_1['results']:
    x = requests.get(i['url']).json()
    pilot = x['result']['properties']['pilots']
    if len(pilot) >= 1:
        new_pilot = pilot
        for n in new_pilot:
            w = requests.get(n).json()
            update_pilot = w['result']['properties']['name']
            print(update_pilot)


