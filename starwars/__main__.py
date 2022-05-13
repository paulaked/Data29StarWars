from app.user_story_1 import StarshipsData
import app.user_story_2 as us2
import app.user_story_3 as us3
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

if __name__ == '__main__':
    # this creates a collection containing starship data
    starships = StarshipsData()
    starships.create_collection()

    # this replaces the pilot urls with a list of associated names
    us2.list_starship()
    us2.replace_urls()

    # this replaces names with object ids of characters
    us3.list_starship()
    us3.replace_names()