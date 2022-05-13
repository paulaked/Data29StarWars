import json
import starwars.config_manager as conf
import requests
import pymongo

# requesting data from api
def get_api(url):
    starship_req = requests.get(url)
    return starship_req

starship_req = requests.get("https://swapi.tech/api/starships").json()
starship_req2 = requests.get("https://www.swapi.tech/api/starships?page=2&limit=10").json()
starship_req3 = requests.get("https://www.swapi.tech/api/starships?page=3&limit=10").json()
starship_req4 = requests.get("https://swapi.tech/api/starships?page=4&limit=10").json()


list = starship_req.get('results')
list2 = starship_req2.get('results')
list3 = starship_req3.get('results')
list4 = starship_req4.get('results')

#getting the urls for all the starships into one list

starship_urls = []
for i in list:
    starship_urls.append(i.get('url'))
for i in list2:
    starship_urls.append(i.get('url'))
for i in list3:
    starship_urls.append(i.get('url'))
for i in list4:
    starship_urls.append(i.get('url'))
#print(starship_urls)

#getting properties for all the starships and changing the urls to names
for url in starship_urls:
    properties = requests.get(url).json()['result']['properties']
    properties['new pilots'] = []
    if properties['pilots'] == []:
        pass
    else:
        for character in properties['pilots']:
            properties['new pilots'].append(requests.get(character).json()['result']['properties']['name'])
    print(properties)




































