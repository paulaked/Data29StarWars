import json
import requests
r = requests.get('https://www.swapi.tech/api/starships')
packages_json = r.json()

packages_str = json.dumps(packages_json, indent=2)
print(packages_str)
