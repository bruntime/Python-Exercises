#guessing game version 2

import random

number = random.randint(0, 75)
num_guess = 8

print ("I'm thinking of a number between 0 and 75. You have %d guesses.") %(num_guess)

user_guess = int(raw_input("What's your guess? "))

guess_total = 0

while guess_total < num_guess:
	guess_total += 1
	if user_guess < number:
		print ("That's incorrect. Go higher.")
		user_guess = int(raw_input("Guess again. "))
	elif user_guess > number:
		print ("That's incorrect. Lower.")
		user_guess = int(raw_input("Guess again. "))
	elif user_guess == number:
		print ("You're correct!!!!")
		break
else:
	print ("I'm sorry. You are out of guesses. The answer was %d.") %(number)
