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