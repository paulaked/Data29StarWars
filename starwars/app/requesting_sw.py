import json
import starwars.config_manager as conf
import requests
import pymongo

# requesting data from api
starship_req = requests.get("https://swapi.tech/api/starships")
starship_re2 = requests.get("https://www.swapi.tech/api/starships?page=2&limit=10")
starship_req3 = requests.get("https://www.swapi.tech/api/starships?page=3&limit=10")
starship_re4 = requests.get("https://swapi.tech/api/starships?page=4&limit=10")

#converting to json files
starship1 = starship_req.json()
starship2 = starship_re2.json()
starship3 = starship_req3.json()
starship4 = starship_re4.json()

#print(starship1)
#print(starship2)
#print(starship3)
#print(starship4)

list = starship1.get('results')
list2 = starship2.get('results')
list3 = starship3.get('results')
list4 = starship4.get('results')

#getting the urls for all the starships
starship_urls = []
for i in list:
    starship_urls.append(i.get('url'))
for i in list2:
    starship_urls.append(i.get('url'))
for i in list3:
    starship_urls.append(i.get('url'))
for i in list4:
    starship_urls.append(i.get('url'))

print(starship_urls)

#getting properties for all the starships
properties_list = []
for url in starship_urls:
    properties_list.append((requests.get(url)).json()['result']['properties']) #appending properties into a list
print(properties_list)

def properties(api_url):
    


























