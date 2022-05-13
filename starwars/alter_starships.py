## EXTRACT STARSHIPS DATASET
import requests
import json




def request_api_online(link):
    return requests.get(link)

starships_req = request_api_online('https://www.swapi.tech/api/starships')
ss_json = starships_req.json()


## TARGET PILOT KEYS VIA API VALUES
def change_pilot_values():
    altered_ss = []
    for i in ss_json['results']:
        get_ss = request_api_online(i['url']).json()
        for k in range(0, len(get_ss['result']['properties']['pilots'])):
            get_id = request_api_online(get_ss['result']['properties']['pilots'][k]).json()['result']['_id']
            get_ss['result']['properties']['pilots'][k] = get_id
            # print(get_name)
            altered_ss.append(get_ss['result'])
        # print(get_ss)
    altered_ss_json = json.dumps(altered_ss)
    print(type(altered_ss_json))
    print(altered_ss_json)
    return altered_ss_json

change_pilot_values()
