import requests
import pymongo
import json

#Access to database 
client = pymongo.MongoClient()
db = client['starwars']

#Created a function to extract data from API link
web_link = 'https://www.swapi.tech/api/starships'
def data(url):
    ship_url = requests.get(url)
    ship_url = ship_url.json() #converted to a JSON file
    return ship_url
starship_page = [value['url'] for value in data(web_link)['results']] #Extracted the first page from my API link

#Function to get all the remaining ships from the different pages
def get_url_for_all_pages():
    page_1 = data(web_link)
    while page_1['next'] != None: # ensuring that the pages i extract give me pages that have data so i ensure that data is not eaual to none
        page_1 = requests.get(page_1['next'])
        page_1 = page_1.json() #coverted to a JSON file
        for item in page_1['results']:
            starship_page.append(item['url'])
    return starship_page


