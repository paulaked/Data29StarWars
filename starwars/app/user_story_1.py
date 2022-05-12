import requests
from requests import Response
import pymongo

# get starships data
# - make request for starships/x where x is each starship
# - need to make sure it can handle the fact that not all x have a starship
# - input - none
# - output - dict


def get_starships_data() -> dict:
    pass


# check data is ready for insert
# - check certain keys exists


def data_ready(data):
    pass


# put data into a collection
# - create collection
# - use insert_many
# - input - dict
# - output - collection


def insert_starships(data):
    pass