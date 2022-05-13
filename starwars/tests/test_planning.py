from starwars.app.requesting_sw import *


def test_extraction():
    assert data(web_address) == dict(data(web_address))


def test_pages_url():
    assert get_url_data_from_all_pages() == list(get_url_data_from_all_pages())


def test_pilots_id():
    assert get_and_replace_pilots_id() == list(get_and_replace_pilots_id())
