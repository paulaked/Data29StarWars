from starwars.app.starships import *


def test_the_source():
    assert get_data(starships_address) == dict(get_data(starships_address))


def test_the_page_urls():
    assert get_all_url() == list(get_all_url())


def test_the_pilots_id():
    assert replace_pilots_with_id() == list(replace_pilots_with_id())


