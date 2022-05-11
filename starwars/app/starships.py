import requesting_sw
import pymongo
import json
import requests

starships_req = requests.get('https://www.swapi.tech/api/starships%27')

y = json.dumps(starships_req)

for i in y:
    print(i)





