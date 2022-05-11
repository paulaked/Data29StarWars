import json

import starwars.config_manager as conf
import requests

starship_req = requests.get("https://swapi.tech/api/starships")
starship_json = starship_req.json()
starship_json_body = json.dumps(starship_json['results'])
print(starship_json_body)

#print(starship_json) #loop through this to get info about starship


