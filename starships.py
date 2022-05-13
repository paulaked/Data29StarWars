from starwars.app.requesting_sw import *

def source_code_test ():
    assert get_request('api_address') == dict(get_request('api_address'))

def test_page_urls ():
    assert collect_urls() == list(collect_urls()

