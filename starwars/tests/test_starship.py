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


if __name__ == '__main__':
    unittest.main()
