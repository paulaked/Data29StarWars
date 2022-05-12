import unittest
from starwars.app import user_story_1

class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = user_story_1.StarshipsData()

    def test_response(self):
        actual = self.data.get_raw_starship_data()
        assert actual == 200







# class UnitTests(unittest.TestCase):
#     def setUp(self) -> None:
#         self.data = user_story_1.get_starship_data()
#
#     def test_response_code(self):
#         assert self.data.status_code == 200

    # def test_type(self):
    #     assert self.data.type == "class"

