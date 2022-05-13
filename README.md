# Data 29 Star Wars Project


### Aim
This repo will return a collection of starships from the Star Wars API, where pilot names will be stored as an array
of object IDs, where the object ID is a reference the relevant Star Wars character from a Characters collection.

### Before using this repo
This repo makes a few assumptions:
1. you have a mongodb database named "starwars"
2. within this database you have a collection named "characters"
3. within that collection you have the properties of all the people from the Star Wars API stored

### Navigating this repo
#### \__main\__.py
Use the __main__.py file to run the program as it will contain only the relevant function/class calls. 

#### app folder
This folder contains all relevant code to run the function and class calls. This in itself is split into three files,
one for each of the user stories (see task board for more info on user stories).

#### tests folder
The tests folder will contain unit test files used for the files in the app folder. Here the tests are again split
into files for the relevant user story code it is testing. Use ```pytest -v``` in terminal to test.


### Task board
https://guttural-waste-40d.notion.site/Star-wars-project-task-56f034f986104eb68443b0721f55ba53
