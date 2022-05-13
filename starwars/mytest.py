## EXTRACT STARSHIPS DATASET
import requests
import json
import pymongo


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
    # print(len(json.loads(json.dumps(altered_ss))))
    # print(json.dumps(altered_ss))
    # return json.loads(json.dumps(altered_ss))
    # return json.dumps(altered_ss)
    return altered_ss

# change_pilot_values(ss_json)


## PUSH NEW COLLECTION TO MONGODB
my_mongo = pymongo.MongoClient('mongodb://localhost:27017')
def add_to_mongo():
    db = my_mongo['starwars']
    print(db.list_collection_names())
    print('-----')
    new_collection = db['starships']
    # new_collection.insert_many(change_pilot_values(ss_json))
    for i in range(0, len(change_pilot_values(ss_json))):
        print(change_pilot_values(ss_json)[i])
        new_collection.insert_one(change_pilot_values(ss_json)[i])
        print('added')
    print('-----')
    print(db.list_collection_names())

add_to_mongo()