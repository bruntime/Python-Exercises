#Guessing Game

import random

guess = int(raw_input("Guess the number between 0 and 5. "))

number = random.randint (0, 5)

#Issue: When user has second guess, does not output whether number is correct or not
#Issue: What if user wants to guess more than twice?
#Better to use while loop and allow certain number of guesses then print out correct answer

if guess < number:
	print "The number is higher. Please try again."
	guess = int(raw_input("It's higher. "))
elif guess > number:
	print "The number is lower. Please try again."
	guess = int(raw_input("It's lower. "))
elif guess == number:
	print "That is correct"
else:
	print "I'm sorry the number is: ", number
	
#Resource: https://docs.python.org/2/library/random.html


