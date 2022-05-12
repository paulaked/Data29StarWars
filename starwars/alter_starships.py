## EXTRACT STARSHIPS DATASET
import requests


def request_api_online(link):
    return requests.get(link)

starships_req = request_api_online('https://www.swapi.tech/api/starships')
ss_json = starships_req.json()


## TARGET PILOT KEYS VIA API VALUES
def change_pilot_values():
    starships_pilot = []
    for i in ss_json['results']:
        for pilot in request_api_online(i['url']).json()['result']['properties']['pilots']:
            # print(request_api_online(pilot).json()['result']['_id'])
            # print('-------')
            pilot = request_api_online(pilot).json()['result']['_id']
            print(pilot)

change_pilot_values()

## REPLACE PILOT KEYS VALUES WITH VALUES FROM CHARACTERS/PEOPLE DATASET
