## EXTRACT STARSHIPS DATASET
import requests


def request_api_online(link):
    return requests.get(link)

starships_req = request_api_online('https://www.swapi.tech/api/starships')
ss_json = starships_req.json()


## TARGET PILOT KEYS VIA API VALUES
def change_pilot_values():
    starships_pilot = ''
    for i in ss_json['results']:
        test = request_api_online(i['url']).json()['result']['properties']['pilots']
        c_pos = 0
        while c_pos < len(test):
            test[c_pos] = request_api_online(test[c_pos]).json()['result']['_id']
            c_pos += 1

        print(test)

    print(starships_pilot)

change_pilot_values()