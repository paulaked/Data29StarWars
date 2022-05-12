## EXTRACT STARSHIPS DATASET
import requests


def request_api_online(link):
    return requests.get(link)

starships_req = request_api_online('https://www.swapi.tech/api/starships')


## TARGET PILOT KEYS VIA API VALUES
## REPLACE PILOT KEYS VALUES WITH VALUES FROM CHARACTERS/PEOPLE DATASET
