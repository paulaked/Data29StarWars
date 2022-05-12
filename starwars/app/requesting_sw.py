import starwars.config_manager as conf
import requests
#hello

sw = requests.get(conf.SWAPI_URL)

