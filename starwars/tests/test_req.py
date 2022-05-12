import unittest
from starwars.app.requesting_sw import *

class UnitTests(unittest.TestCase):
    # def test_api(self):
    #     result = api("https://www.swapi.tech/api/starships/").status_code
    #     self.assertEqual(result, 200)

    def test_empty_response(self):
        actual = total_valid("https://www.swapi.tech/api/starships/")
        expected = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17, 21, 22, 23, 27, 28, 29, 31, 32]
        self.assertEqual(actual, expected, "Expected to return a list of the starships that exists")

    #testing a function which returns the ships that do not have any pilots
    def test_pilots(self):
        valid_ships = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17, 21, 22, 23, 27, 28, 29, 31, 32]
        actual = no_pilots(valid_ships,"https://www.swapi.tech/api/starships/")
        expected = ['CR90 corvette', 'Star Destroyer', 'Sentinel-class landing craft', 'Death Star', 'Y-wing',
                    'Executor', 'Rebel transport', 'EF76 Nebulon-B escort frigate', 'Calamari Cruiser', 'B-wing',
                    'Republic Cruiser', 'Droid control ship']
        self.assertEqual(actual, expected)
    #testing the function that returns the ships with the pilot urls
    def test_ships_pilots(self):
        valid_ships = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17, 21, 22, 23, 27, 28, 29, 31, 32]
        actual = star_ships(valid_ships,"https://www.swapi.tech/api/starships/")
        expected ={'Millennium Falcon': ['https://www.swapi.tech/api/people/13', 'https://www.swapi.tech/api/people/14',
                                         'https://www.swapi.tech/api/people/25', 'https://www.swapi.tech/api/people/31'],
                   'X-wing': ['https://www.swapi.tech/api/people/1', 'https://www.swapi.tech/api/people/9',
                              'https://www.swapi.tech/api/people/18', 'https://www.swapi.tech/api/people/19'],
                   'TIE Advanced x1': ['https://www.swapi.tech/api/people/4'],
                   'Slave 1': ['https://www.swapi.tech/api/people/22'],
                   'Imperial shuttle': ['https://www.swapi.tech/api/people/1', 'https://www.swapi.tech/api/people/13',
                                        'https://www.swapi.tech/api/people/14'],
                   'A-wing': ['https://www.swapi.tech/api/people/29']}
        self.assertEqual(actual, expected)


    def test_ships_pilot_id(self):
       actual = get_pilots({'Millennium Falcon': ['https://www.swapi.tech/api/people/13',
                                                  'https://www.swapi.tech/api/people/14',
                                                  'https://www.swapi.tech/api/people/25',
                                                  'https://www.swapi.tech/api/people/31'],
                            'X-wing': ['https://www.swapi.tech/api/people/1', 'https://www.swapi.tech/api/people/9',
                                       'https://www.swapi.tech/api/people/18', 'https://www.swapi.tech/api/people/19'],
                            'TIE Advanced x1': ['https://www.swapi.tech/api/people/4'],
                            'Slave 1': ['https://www.swapi.tech/api/people/22'],
                            'Imperial shuttle': ['https://www.swapi.tech/api/people/1',
                                                 'https://www.swapi.tech/api/people/13',
                                                 'https://www.swapi.tech/api/people/14'],
                            'A-wing': ['https://www.swapi.tech/api/people/29']})

       expected = {'Millennium Falcon': ['5f63a36eee9fd7000499be4e', '5f63a36eee9fd7000499be4f',
                                             '5f63a36fee9fd7000499be59', '5f63a36fee9fd7000499be5f'],
                       'X-wing': ['5f63a36eee9fd7000499be42', '5f63a36eee9fd7000499be4a', '5f63a36fee9fd7000499be52',
                                    '5f63a36fee9fd7000499be53'], 'TIE Advanced x1': ['5f63a36eee9fd7000499be45'],
                       'Slave 1': ['5f63a36fee9fd7000499be56'],
                       'Imperial shuttle': ['5f63a36eee9fd7000499be42', '5f63a36eee9fd7000499be4e',
                                            '5f63a36eee9fd7000499be4f'],
                       'A-wing': ['5f63a36fee9fd7000499be5d']}

       self.assertEqual(actual, expected)












if __name__ == '__main__':
    unittest.main() # Replace this with code to run your app
