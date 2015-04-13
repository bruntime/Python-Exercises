#Project - Animal Crossing (segment)
#Animal Crossing is a popular Nintendo game
#I will not attempt to recreate the whole game.
#However I will try putting together some portions of the game

#creating a new character

def name_choice(name):

	print 'Nice name! I like it!'
	
	response = 0
	character = 0
	
	if response == "Cool, eh?":
		character == 'boy'
		print "You are a ", character, ". Is this correct?"
	if response == "Cute, hm?":
		character == 'girl'
		print "You are a ", character, ". Is this correct?"
	if response == "That's not it.":
		print "What is your name again?"
		name = raw_input("My name is ")
	
print "What is your name?"

name_user = raw_input("My name is ")

name_choice(name_user)