from app.user_story_1 import StarshipsData
import app.user_story_2 as us2
import app.user_story_3 as us3
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]

if __name__ == '__main__':
    starships = StarshipsData()
    starships.create_collection()
    # we have now created a collection containing starship data

    us2.list_starship()
    us2.replace_urls()
    # we have now replaced the pilot urls with a list of associated names

    us3.list_starship()
    us3.replace_names()


    pass  # Replace this with code to run your app
