import unittest
import requests
import json
import alter_starships

class TestAlterStarships(unittest.TestCase):
    def setUp(self) -> None:
        self.starship_json = requests.get('https://www.swapi.tech/api/starships').json()
        self.altered_ss_comparison = alter_starships.change_pilot_values(self.starship_json)

    def test_request_api_online(self):
        result = alter_starships.request_api_online('https://www.swapi.tech/api/starships')
        self.assertEqual(result.status_code, 200)


    def test_change_pilot_values(self):
        result = alter_starships.change_pilot_values(self.starship_json)
        self.assertEqual(result, self.altered_ss_comparison)