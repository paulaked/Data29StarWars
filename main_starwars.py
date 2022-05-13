# import json
# import requests

# # FUNCTION TO PULL ALL AVAILIBLE STARSHIPS FROM API
# starship_request = requests.get('https://www.swapi.tech/api/starships') # pull data from an API file
# starship_json = starship_request.json()
# characters_request = requests.get('https://www.swapi.tech/api/people')
# characters_json = characters_request.json() #requesting a json object of the result

# starship_str = json.dumps(starship_json) #converting the a json file
# characters_str = json.dumps(characters_json)
# #FUNCTION TO CHECK INTO THE URL AND EXTRACT ALL STARSHIPS TO EXTRACT ALL AVAILIBLE DATA
# for package in starship_json['results']:
#     print(requests.get(package["url"]).json()) 

# print(characters_str) #extracted all characters from the data to have also the ID's


# 1. Ensure that imports from python library are set:
import requests
import pymongo
import json

# 2.Access to database 
client = pymongo.MongoClient()
db = client['starwars']

#Created a function to extract data from API link
website = 'https://www.swapi.tech/api/starships'
def data(url):
    starship_url = requests.get(url)
    starship_url = starship_url.json()
    return starship_url

starship_page = [value['url'] for value in data(website)['results']]


def get_url_for_all_pages():
    current_page = data(website)
    while current_page['next'] != None:
        current_page = requests.get(current_page['next'])
        current_page = current_page.json()
        for item in current_page['results']:
            starship_page.append(item['url'])
    return starship_page


