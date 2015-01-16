#guessing game version 2

import random

number = random.randint(0, 75)
num_guess = 8
guess_total = 2 #initializes at 2 because technically first guess is not within loop

print ("I'm thinking of a number between 0 and 75. You have %d guesses.") %(num_guess)

user_guess = int(raw_input("What's your guess? "))

while guess_total < num_guess:
	guess_total += 1
	if user_guess < 0 or user_guess > 75:
		print ("That number is not within range.")
	if user_guess < number:
		print ("That's incorrect. Go higher.")
		user_guess = int(raw_input("Guess again. "))
	if user_guess > number:
		print ("That's incorrect. Lower.")
		user_guess = int(raw_input("Guess again. "))
	if guess_total == 8:
		user_guess = int(raw_input("This is your last guess. "))
	if user_guess == number:
		print ("You're correct!!!!")
		break
else:
	print ("I'm sorry. You are out of guesses. The answer was %d.") %(number)