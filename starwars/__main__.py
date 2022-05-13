from app.requesting_sw import *
from app.database import *
import json

# Gets the ships that are available from the api.
valid_ships = total_valid_ships("https://www.swapi.tech/api/starships/")
# gets the urls of the pilots.
ships = star_ships_pilot_url(valid_ships)
# get the name of the pilots through the url.
ships_with_pilots = get_pilots_name(ships)
#returns a list of all the ships with the pilots names
final_ships = all_ships(valid_ships, ships_with_pilots)

#Stores all the transormed data in a json file
with open("all_ships.json", "w") as jsonfile:
    json.dump(final_ships, jsonfile)

f = open('all_ships.json')
data = json.load(f)
f.close()
# The function below creates an empty 'starwships' collection
creating_starships()
# the json file which stores the starships data is accessed and passed to the function below
# adding all the ships to the 'starships' collection
add_ships_data(data)


if __name__ == '__main__':
    pass  # Replace this with code to run your app