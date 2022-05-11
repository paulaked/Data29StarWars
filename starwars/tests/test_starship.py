import unittest
from starwars.starships import Starships


class MyTestCase(unittest.TestCase):

    # Calls starships class to be tested
    def setUp(self) -> None:
        self.starships = Starships()

    # Tests if requests gives a dictionary as a response
    def test_request(self) -> None:
        actual = self.starships.requesting()
        self.assertEqual(type(actual), dict, "Type Check Failed: Dictionary expected")


if __name__ == '__main__':
    unittest.main()
