# Data 29 Star Wars Project

## Instructions

The character data in your MongoDB database has been pulled from https://swapi.tech/.
As well as 'people', the API has data on starships.
Using Python, write code to pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship.
Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection in MongoDB.
(Make sure you drop any existing starships collections.)

You have until Friday EOD.

## Requirements

- Use good coding principles.  That means testing, appropriate comments, good naming conventions and handling errors gracefully.
- Follow PEP 8
- Create a job board in Trello or similar to keep track of your user stories.  Provide a link to that job board in your version of this README.
- Your code should utilise functional programming OR object-oriented programming
- Use Test Driven Development: write your tests first
- Good use of Git and GitHub. Commit and push often with meaningful commit messages.
- Include an appropriate version of this README

## Infomation
In order for this code to work you will need to have a database in mongo db named 'starwars' with a collection named 'characters' which include the data on 87 star wars charaters.

The code creates a collection called starships which includes all the star ships that can be attained through the api mentioned above.
The collection also includes star ships that don't have registered pilots and where there are pilots for the ships the pilot's ObjectID are present. 

To execute the code run the _main_.py file.
Functions are used and imported in the main file, the functions that are used to get the star ships data from the api are located in the app folder, in the requesting_sw.py file. Additionally, the functions used to add the 'starship' collection to the database can be found in the database.py file. Testing has been done using unit testing and they have all passed, they can be found in the test_starwars.py file. Planning was
done using a job board which is linked below. 


## My Job Board 
https://trello.com/b/8JaVhobU/star-wars