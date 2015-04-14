#Project - Animal Crossing (segment)
#Animal Crossing is a popular Nintendo game
#I will not attempt to recreate the WHOLE game.
#However I will try putting together some portions of the game

#creating a new character

from animal_crossing_functions import intro
from animal_crossing_functions import name_choice

print intro()

name_user = raw_input("My name is ")
name_choice(name_user)