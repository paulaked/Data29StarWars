import requests
import json


star_ship_req = requests.get("https://www.swapi.tech/api/starships")

star_ship_req_dict = star_ship_req.json()

# with open("star_wars_1","w") as jsonfile:
#     json.dump(star_ship_req_dict, jsonfile)

print(star_ship_req_dict)

