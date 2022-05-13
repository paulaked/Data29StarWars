# Tobi Salami's Star Wars Project

## Aim

The aim of this project is to be able to pull Starship data from the Star Wars API (https://swapi.tech/) and import this data into a MongoDB database. This is done through the use of object oriented programming alongside Test Driven Development (TDD). For further information of aims and user stories go to:
https://trello.com/starwarsproject12

## Using this repository

### 1. Requirements and Pre-requisites:

1.1

Python 3.9 with these packages installed:
- pymongo
- requests

A mongoDB database with a database called 'starwars'. Within 'starwars' must be the collection 'characters'. Within the collection 'characters' must be all the appropriate documents of characters collected from the Star Wars API. 



### 2. Running files

Run the '_main_.py' file only. 'starships.py' contains all class methods and attributes. Testing for class attributes is in 'test_starship.py', located within the 'tests' subfolder.

## Notes

Duplicates of starship documents can be made. In order to remove duplicates, delete starships collection and run '_main_.py' once.


## Test Notes


Testing modules that interact with mongoDB requires dummy files. A replica of the 'starwars' database was made named 'test_starwars' only containing character info for Han Solo with the Starship: Millennium Falcon. NB this starship only contains the Han Solo as one of the pilots. The last two test in test_starship.py ('test_add_starships_docs' and 'test_id_replace') are hard coded and require this specific set-up to run properly. They must be run in the order given to work properly as files are written in these tests. 

