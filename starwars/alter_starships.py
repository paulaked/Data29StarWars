## EXTRACT STARSHIPS DATASET
import requests


def get_api_online(link):
    return requests.get(link)

starships_req = get_api_online('https://www.swapi.tech/api/starships')
characters_req = get_api_online('https://www.swapi.tech/api/people')




## EXTRACT PEOPLE DATASET
## TARGET PILOT KEYS VIA API VALUES
## REPLACE PILOT KEYS VALUES WITH VALUES FROM CHARACTERS/PEOPLE DATASET
