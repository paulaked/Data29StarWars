import requests


def get_starship_data() -> list:
    return requests.get("https://swapi.tech/api/starships").json()["results"]

starships_list = get_starship_data()

def get_starships_urls(list) -> list:
    url_list = []
    for starship in list:
        url_list.append(starship["url"])
    return url_list

url_list = get_starships_urls(starships_list)

def get_pilot_data(list) -> list:
    pilot_data = []
    for starship in list:
        pilot_data.append({"ship_name": requests.get(starship).json()["result"]["properties"]["model"],
                           "pilot_urls": requests.get(starship).json()["result"]["properties"]["pilots"]
                        })
    return pilot_data

pilot_data = get_pilot_data(url_list)
print(pilot_data)