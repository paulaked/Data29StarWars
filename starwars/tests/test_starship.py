import unittest
from starwars.starships import Starships
import pymongo



class MyTestCase(unittest.TestCase):

    # Calls starships class to be tested
    def setUp(self) -> None:
        self.starships = Starships()

    # Tests if requests gives a dictionary as a response
    def test_request(self):
        actual = self.starships.requesting()
        self.assertEqual(type(actual), dict, "Type Check Failed: Dictionary expected")
        self.assertIsNotNone(actual, "Dictionary is empty")

    # Tests if next page gives a greater amount of content back and is appending to the results dict
    def test_get_next_page(self):
        self.starships.content = {
    "count": 36,
    "next": "https://swapi.dev/api/starships/?page=2",
    "previous": "",
    "results": [
        {
            "name": "CR90 corvette",
            "model": "CR90 corvette",
            "manufacturer": "Corellian Engineering Corporation",
            "cost_in_credits": "3500000",
            "length": "150",
            "max_atmosphering_speed": "950",
            "crew": "30-165",
            "passengers": "600",
            "cargo_capacity": "3000000",
            "consumables": "1 year",
            "hyperdrive_rating": "2.0",
            "MGLT": "60",
            "starship_class": "corvette",
            "pilots": [],
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-10T14:20:33.369000Z",
            "edited": "2014-12-20T21:23:49.867000Z",
            "url": "https://swapi.dev/api/starships/2/"
        }]}
        next_page = "https://swapi.dev/api/starships/?page=2"
        page_content = self.starships.get_url(next_page)
        output = self.starships.get_next_page(next_page)
        self.assertGreater(len(output['results']),len(page_content['results']),
                           'Content was not added to results dictionary')

    # Tests if get starships gives a list as a response
    def test_get_starships(self):
        self.starships.requesting()
        actual = self.starships.get_starships()
        self.assertEqual(type(actual), list, "Type Check Failed: List expected")
        self.assertIsNotNone(actual, "List is empty")

    # Tests if get_url gives a dictionary as a response
    def test_get_url(self):
        self.assertEqual(type(self.starships.get_url('https://www.swapi.tech/api/people/13')), dict,
                         "Type Check Failed: Dictionary expected")

    # Tests if empty pilots returns none
    def test_empty_pilots(self):
        ship = {'model': 'CR90 corvette', 'starship_class': 'corvette',
                'manufacturer': 'Corellian Engineering Corporation',
                'cost_in_credits': '3500000',
                'length': '150', 'crew': '30-165',
                'passengers': '600', 'max_atmosphering_speed': '950',
                'hyperdrive_rating': '2.0', 'MGLT': '60', 'cargo_capacity': '3000000',
                'consumables': '1 year', 'pilots': [],
                'created': '2020-09-17T17:55:06.604Z', 'edited': '2020-09-17T17:55:06.604Z',
                'name': 'CR90 corvette', 'url': 'https://www.swapi.tech/api/starships/2'}
        self.starships.empty_pilots(ship)
        self.assertIs(ship["pilots"], None, "Value must be None")

    # Tests if pilots exists returns not an empty list
    def test_pilots_exist(self):
        ship = {'model': 'YT-1300 light freighter', 'starship_class': 'Light freighter',
                'manufacturer': 'Corellian Engineering Corporation', 'cost_in_credits': '100000',
                'length': '34.37', 'crew': '4', 'passengers': '6', 'max_atmosphering_speed': '1050',
                'hyperdrive_rating': '0.5', 'MGLT': '75', 'cargo_capacity': '100000',
                'consumables': '2 months',
                'pilots': ['https://www.swapi.tech/api/people/13', 'https://www.swapi.tech/api/people/14',
                           'https://www.swapi.tech/api/people/25', 'https://www.swapi.tech/api/people/31'],
                'created': '2020-09-17T17:55:06.604Z', 'edited': '2020-09-17T17:55:06.604Z',
                'name': 'Millennium Falcon', 'url': 'https://www.swapi.tech/api/starships/10'}
        initial_len = len(ship["pilots"])
        self.starships.pilots_exist(ship)
        self.assertIsNotNone(ship["pilots"], "Values cannot be none")
        self.assertIs(type(ship["pilots"]), list, "Must be a list")
        self.assertEqual(initial_len, len(ship["pilots"]), "Initial length of list,"
                                                           " doesn't match current list length")


if __name__ == '__main__':
    unittest.main()
