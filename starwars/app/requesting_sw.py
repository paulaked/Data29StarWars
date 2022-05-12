# 1. Import necessary python libraries:
import requests
import pymongo
import json

# 2. Connecting and using starwars database on Mongocb:
client = pymongo.MongoClient()
db = client['starwars']

# starship API address:
web_address = 'https://www.swapi.tech/api/starships'


# 3. The following function extract the data from the corresponding API address:
def extract_data(url):
    starship_url = requests.get(url)
    starship_url = starship_url.json()
    return starship_url

# 4. The urls for the first page is stored as a list:
starship_page = [value['url'] for value in extract_data(web_address)['results']]


# 5. The following function extract the starship's urls for pages 2,3 and 4 and add them to the previous list:
def get_url_for_all_pages():
    current_page = extract_data(web_address)
    while current_page['next'] != None:
        current_page = requests.get(current_page['next'])
        current_page = current_page.json()
        for item in current_page['results']:
            starship_page.append(item['url'])
    return starship_page




