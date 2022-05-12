from starships import Starships

if __name__ == '__main__':
    starships = Starships()
    starships.requesting()
    starships.get_starships()
    starships.get_ship_info()
    starships.get_pilot_info()
    starships.create_collection()
    starships.add_starships_docs()
    starships.id_replace()