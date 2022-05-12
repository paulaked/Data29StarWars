import unittest
from starwars.starships import Starships


class MyTestCase(unittest.TestCase):

    # Calls starships class to be tested
    def setUp(self) -> None:
        self.starships = Starships()

    # Tests if requests gives a dictionary as a response
    def test_request(self):
        actual = self.starships.requesting()
        self.assertEqual(type(actual), dict, "Type Check Failed: Dictionary expected")
        self.assertIsNotNone(actual, "Dictionary is empty")

    # Tests if requests gives a dictionary as a response
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
        self.starships.pilots_exist(ship)
        self.assertIsNotNone(ship["pilots"], "Values cannot be none")
        self.assertIs(type(ship["pilots"]), list, "Must be a list")


if __name__ == '__main__':
    unittest.main()
