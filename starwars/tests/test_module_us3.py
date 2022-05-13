import unittest
from starwars.app import user_story_3 as us3
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]


class UnitTests(unittest.TestCase):

    def setUp(self) -> None:
        self.list = us3.list_starship()

    def test_list_starship(self):
        actual = len(self.list)
        expected = 36
        self.assertEqual(actual, expected, "Expected 36 entries in list")

    def test_replace_names_type(self):
        actual = type((db.starships.find_one({"uid": "10"}, {"_id":0, "properties.pilots": 1}))["properties"]["pilots"])
        expected = list
        self.assertEqual(actual, expected, "Value in pilot field after replacement should be of type list")

    def test_replace_names(self):
        from bson.objectid import ObjectId
        actual = db.starships.find_one({"uid": "10"}, {"_id":0, "properties.pilots": 1})["properties"]["pilots"]
        expected = [ObjectId('627a6757f2a9f31fad6e96b5'),
                   ObjectId('627a6763abe3f652f07c9145'),
                   ObjectId('627a676a9319f863bb9b3005'),
                   ObjectId('627a6770f42d90cfaa70d2fd')]
        self.assertEqual(actual, expected, "Check object ids are as expected")