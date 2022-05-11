import unittest
from starwars.starships import Starships

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.starships = Starships()

    def test_request(self) -> None:
        actual = self.starships.requesting()
        self.assertEqual(type(actual),dict, "Type Check Failed: Dictionary expected")

if __name__ == '__main__':
    unittest.main()
