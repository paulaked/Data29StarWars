#import requesting_sw
#import pymongo
#import json
#import requests

#client = pymongo.MongoClient()
#db = client["starwars"]

#db.drop_collection("starships")

#starships_req = requests.get("https://www.swapi.tech/api/starships")
#characters_req = requests.get("https://www.swapi.tech/api/people")


#starships_req_json = starships_req.json()

#characters_req_json = characters_req.json()


#print(starships_req_json["results"])

#for i in starships_req_json['results']:
#    print(i['url'])

#def get_url():
#starship_urls = []

#for i in starships_req_json['results']:
#    print(requests.get(i['url']).json())
    #starships_urls.append(requests.get(i['url']).json())

#urls_list = []

#def get_urls():
 #   for i in starships_req_json["results"]:
  #      urls = requests.get(i['url']).json()
   #     print(urls["result"]['properties']['pilots'])

#def get_people():
#    for i in characters_req_json['results']:
#        print(requests.get(i['_id']).json())


#{'message': 'ok', 'result': {'properties': {'model': 'CR90 corvette', 'starship_class': 'corvette', 'manufacturer': 'Corellian Engineering Corporation', 'cost_in_credits': '3500000', 'length': '150', 'crew': '30-165', 'passengers': '600', 'max_atmosphering_speed': '950', 'hyperdrive_rating': '2.0', 'MGLT': '60', 'cargo_capacity': '3000000', 'consumables': '1 year', 'pilots': [], 'created': '2020-09-17T17:55:06.604Z', 'edited': '2020-09-17T17:55:06.604Z', 'name': 'CR90 corvette', 'url': 'https://www.swapi.tech/api/starships/2'}, 'description': 'A Starship', '_id': '5f63a34fee9fd7000499be1e', 'uid': '2', '__v': 0}}



#for i in urls_list:
 #   properties = requests.get(i["result"]).json()
  #  print(properties)


#print(starships_urls)

#for i in starships_req_json['results']['properties']:
#    print(requests.get(i['pilots']).json())

#for i in characters_req_json['results']:
 #   print(requests.get(i['url']).json())

#for i in characters_req_json['results']:
#    print(requests.get(i['_id']).json())


# not urls, object ids of database

#temp_ships = []
#temp_pilots = []
#x = starships_req_json["result"]["properties"]["name"]
#pilots = starships_req_json["result"]["properties"]["pilots"]
#if pilots != 0:
#    for i in range(0,len(pilot)):
#        temp_ships.append(x)
#        temp_pilots.append(pilots[i])
#else:
#    print(x + "no pilot")

#get_urls()

