import unittest
from starwars.app import user_story_1 as us1

class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test = us1.StarshipsData()

    def test_starships_url_list(self):
        self.test.get_raw_starship_data()
        self.test.starships_url_list()
        actual = len(self.test.url_list)
        expected = 36
        self.assertEqual(actual, expected, "Expected list to contain 36 entries")

    def test_get_starships_data(self):
        self.test.get_raw_starship_data()
        self.test.starships_url_list()
        self.test.get_starships_data()
        actual = type(self.test.starships_data)
        expected = list
        self.assertEqual(actual, expected, "Data returned should be in list form ready for insert to collection")