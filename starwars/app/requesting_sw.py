import starwars.config_manager as conf
import requests

# def api(url):
#     sw = requests.get(url)
#     return sw
# sw = requests.get(conf.SWAPI_URL)
# sw = requests.get("https://www.swapi.tech/api/starships/9")


def total_valid(url):
    valid = []
    sw = requests.get(url).json()
    total = sw["total_records"]
    # gets the total number of star ships
    for i in range(1, total+1):
        sws = requests.get(url+str(i))
        if sws.status_code != 404:
            valid.append(i)
    #get the numbers of the valid star ships
    return valid


#valid = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17, 21, 22, 23, 27, 28, 29, 31, 32]

def no_pilots(ships, url):
    no_pilots = []
    for i in ships:
        sw = requests.get(url+str(i))
        data = sw.json()
        ship_name = data["result"]["properties"]["name"]
        pilot = data["result"]["properties"]["pilots"]
        if len(pilot) <= 0:
            no_pilots.append(ship_name)
    return no_pilots

#
#no_pilots_ships = no_pilots(valid,"https://www.swapi.tech/api/starships/")

def star_ships(ships, url):
    ships_pilots = {}
    for i in ships:
        temp = []
        sw = requests.get(url+str(i))
        data = sw.json()
        ship_name = data["result"]["properties"]["name"]
        pilot = data["result"]["properties"]["pilots"]
        if len(pilot) > 0:
            for num in range(0, len(pilot)):
                temp.append(pilot[num])
            ships_pilots[ship_name] = temp
    return ships_pilots

# print(star_ships(valid,"https://www.swapi.tech/api/starships/"))


def get_pilots(test):
    ships_pilot_id = {}
    for ships in test:
        temp = []
        for pilot in range(0, len(test[ships])):
            p = requests.get(test[ships][pilot]).json()
            pp=p["result"]["_id"]
            temp.append(pp)
        ships_pilot_id[ships] = temp
    return ships_pilot_id

valid = total_valid("https://www.swapi.tech/api/starships/")
print(get_pilots(star_ships(valid, "https://www.swapi.tech/api/starships/")))



























# for i in valid:
#     sw = requests.get("https://www.swapi.tech/api/starships/"+str(i))
#     data = sw.json()
#     print(data)