#a test to check if the correct type of information is extracted
url = starship_req = requests.get("https://swapi.tech/api/starships")

def test_get_api():
    assert type(get_api(url)) is dict