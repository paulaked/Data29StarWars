import unittest
import alter_starships

class TestAlterStarships(unittest.TestCase):

    def test_request_api_online(self):
        result = alter_starships.request_api_online('https://www.swapi.tech/api/starships')
        # self.assertEqual(result, '<Response [200]>')
        self.assertEqual(result.status_code, 200)
