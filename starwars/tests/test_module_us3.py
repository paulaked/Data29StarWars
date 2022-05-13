import unittest
from starwars.app import user_story_3 as us3

client = pymongo.MongoClient()
db = client["starwars"]

class UnitTests(unittest.TestCase):

    def setUp(self) -> None:
        self.list = us3.list_starship()

    def test_list_starship(self):
        actual = len(self.list)
        expected = 36
        self.assertEqual(actual, expected, "Expected 36 entries in list")

    def test_replace_names(self):
        test_character = db["test_character"]
        test_starship = db["test_starship"]
        db.test_character.insert({"name": "test pilot"})
        db.test_starship.insert({"name": "starship 1", "pilot": "test pilot"})

        self.replace = us3.replace_names()

        actual = db.test_starship.find_one({"name":"starship 1"}, {"pilot":1}).json()
        expected = db.test_character.find_one({"name":"test pilot"}, {"_id":1}).json()

        test_character.drop()
        test_starship.drop()
        
        self.assertEqual(actual, expected, "Object id matches with that of the ")

