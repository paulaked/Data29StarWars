from definitions import PROJECT_ROOT_DIR
import configparser
import os

_config = configparser.ConfigParser()

_config.read(os.path.join(PROJECT_ROOT_DIR, 'config.ini'))

SWAPI_URL = _config['default']['url']
STARSHIPS_SWAPI_URL = _config['default']['starships_url']
PEOPLE_SWAPI_URL = _config['default']['people_url']

