import starwars.config_manager as conf
import requests
import json

# sw = requests.get("https://www.swapi.tech/api/starships")
#
# sw_1 = sw.json()
# starships_1 = []
# for i in sw_1['results']:
#     x = requests.get(i['url']).json()
#     pilot = x['result']['properties']
#     starships_1.append(pilot)
# print(starships_1)
#
#
# for i in starships_1:
#     i['pilot'] = 'ships'
# print(starships_1)
#
#
#
#
# for i in sw_1['results']:
#     x = requests.get(i['url']).json()
#     pilot = x['result']['properties']['pilots']
#     if len(pilot) >= 1:
#         new_pilot = pilot
#         for n in new_pilot:
#             w = requests.get(n).json()
#             update_pilot = w['result']['properties']['name']
sw = requests.get("https://www.swapi.tech/api/starships")

sw_1 = sw.json()
starships_1 = []
for i in sw_1['results']:
    x = requests.get(i['url']).json()
    pilot = x['result']['properties']
    starships_1.append(pilot)
print(starships_1)



for i in starships_1:
    x = requests.get(i['url']).json()
    pilot = x['result']['properties']['pilots']
    if len(pilot) >= 1:
        new_pilot = pilot
        pilots = []
        for n in new_pilot:

            w = requests.get(n).json()
            update_pilot = w['result']['properties']['name']
            pilots.append(update_pilot)
        i["pilots"] = pilots

print(starships_1)





