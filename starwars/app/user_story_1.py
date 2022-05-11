import starwars.config_manager as conf
import requests
import json


def get_starship_data():
    return requests.get("https://swapi.tech/api/starships")


starship_data = get_starship_data().json()["results"]
print(starship_data)
