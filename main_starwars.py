import json
import requests

# FUNCTION TO PULL ALL AVAILIBLE STARSHIPS FROM API
starship_request = requests.get('https://www.swapi.tech/api/starships')
starship_json = starship_request.json()
characters_request = requests.get('https://www.swapi.tech/api/people')
characters_json = characters_request.json() #requesting a json object of the result

starship_str = json.dumps(starship_json) #converting the a json file
characters_str = json.dumps(characters_json)
print(starship_str)
print(characters_str) #extracted all characters from the data to have also the ID's

#FUNCTION TO CHECK INTO THE URL AND EXTRACT ALL STARSHIPS TO EXTRACT ALL AVAILIBLE DATA
for i in starship_json['results']:
    print(requests.get(i["url"]).json()) 

