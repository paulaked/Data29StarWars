import unittest
from starwars.starships import Starships

class test (unittest.test):
    def setUp(self) -> None:
        self.starships = Starships()


# if __name__ == '__main__':
#     unittest.main()