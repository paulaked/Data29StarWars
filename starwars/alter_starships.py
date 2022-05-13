## EXTRACT STARSHIPS DATASET
import requests
import json


def request_api_online(link):
    return requests.get(link)

starships_req = request_api_online('https://www.swapi.tech/api/starships')
ss_json = starships_req.json()


## TARGET PILOT KEYS VIA API VALUES
def change_pilot_values(json_object):
    altered_ss = []
    for i in json_object['results']:
        get_ss = request_api_online(i['url']).json()
        for k in range(0, len(get_ss['result']['properties']['pilots'])):
            get_id = request_api_online(get_ss['result']['properties']['pilots'][k]).json()['result']['_id']
            get_ss['result']['properties']['pilots'][k] = get_id
            altered_ss.append(get_ss['result'])

    return json.dumps(altered_ss)

change_pilot_values(ss_json)
