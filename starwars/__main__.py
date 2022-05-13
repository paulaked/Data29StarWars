from app.requesting_sw import *
from app.database import *
import json


valid_ships = total_valid_ships("https://www.swapi.tech/api/starships/")
# Gets the ships that are available from the api
ships = star_ships_pilot_url(valid_ships)
ships_with_pilots = get_pilots_name(ships)# ships linked with pilots name
final_ships = all_ships(valid_ships, ships_with_pilots) # add all the valid ships in a list of dictionaries

#Stores all the transormed data in a json file
with open("all_ships.json", "w") as jsonfile:
    json.dump(final_ships, jsonfile)

f = open('all_ships.json')
data = json.load(f)
f.close()
# The function below creates an empty 'starchips' collection
creating_starships()
# the json file is accessed and passed the function adding all the ships to the 'starships' collection
add_ships_data(data)


if __name__ == '__main__':
    pass  # Replace this with code to run your app