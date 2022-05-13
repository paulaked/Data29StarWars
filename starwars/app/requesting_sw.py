#import starwars.config_manager as conf
import requests


# This function gets all the valid ships from the api and returns them as list
def total_valid_ships(url):
    all_ships = []
    sw = requests.get(url)
    sw = sw.json()
    total = sw["total_records"]
    # gets the total number of star ships from the api
    for i in range(1, total+1):
        sws = requests.get(url+str(i))
        # requests the starships/1 starships/2 starships/3 etc...
        data = sws.json()
        if sws.status_code != 404:
            # if the response from the api is not empty it will add it to the all_ships list
            all_ships.append(data["result"]["properties"])
    return all_ships


# The function below gets all the ships that have a pilot and return a dictionary that has the ships names as keys and
# the values are the urls.
def star_ships_pilot_url(ships):
    ships_pilots = {}
    for i in ships:
        pilot_url = [] # keeps a list of the pilots url.
        ship_name = i["name"] # get the name of the ship that the loop is iterating through.
        pilot = i["pilots"] # get the list of pilot urls.
        if len(pilot) > 0:
            # if the ship has pilots it executes the code below.
            for num in range(0, len(pilot)): # for each url in the list it is appended to the pilot_url list.
                pilot_url.append(pilot[num])
            ships_pilots[ship_name] = pilot_url # with the ship name being the key the pilot urls are assigned as the values.
    return ships_pilots



# This function gets the name of the pilot and links it with the ship
def get_pilots_name(ship_dict):
    ships_pilot= {}
    for ships in ship_dict:
        pilot_names = []
        for pilot in range(0, len(ship_dict[ships])):
            pilot_url = requests.get(ship_dict[ships][pilot])
            p = pilot_url.json()
            pilot_name = p["result"]["properties"]["name"]
            pilot_names.append(pilot_name)
        ships_pilot[ships] = pilot_names

    return ships_pilot

# this functions returns a list of all the ships. Where when the ship has a pilot the name of the pilot is stored
# instead of the url.

def all_ships(all_ships, ships_with_pilots):
    ship_names = []
    for names in ships_with_pilots:
        ship_names.append(names)
    for i in range(0, len(all_ships)):
        if all_ships[i]["name"] in ship_names:
            z = ships_with_pilots.get(all_ships[i]["name"])
            all_ships[i]["pilots"] = z
    return all_ships
































# # {'Millennium Falcon': ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb'],
# #  'X-wing': ['Luke Skywalker', 'Biggs Darklighter', 'Wedge Antilles', 'Jek Tono Porkins'],
# #  'TIE Advanced x1': ['Darth Vader'],
# #  'Slave 1': ['Boba Fett'],
# #  'Imperial shuttle': ['Luke Skywalker', 'Chewbacca', 'Han Solo'],
# #  'A-wing': ['Arvel Crynyd']}
#






















# for i in valid:
#     sw = requests.get("https://www.swapi.tech/api/starships/"+str(i))
#     data = sw.json()
#     print(data)