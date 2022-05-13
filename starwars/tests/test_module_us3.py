import unittest
from starwars.app import user_story_3 as us3

client = pymongo.MongoClient()
db = client["starwars"]

class UnitTests(unittest.TestCase):

    def setUp(self) -> None:
        self.list = us3.list_starship()
        # self.replace = us3.replace_names()

    def test_list_starship(self):
        actual = len(self.list)
        expected = 36
        self.assertEqual(actual, expected, "Expected 36 entries in list")

    def test_replace_names(self):

        actual = db.starships.find_one({"uid": "10"}, {"properties.pilots":1}).json()
        expected = []