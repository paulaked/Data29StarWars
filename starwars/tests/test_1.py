from starwars.app.requesting_sw import *


def extracting_starships():
    assert get_starships(sw_1) == dict(get_starships(sw_1))
