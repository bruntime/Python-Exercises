#Define a function max_of_three() that takes three numbers and returns the largest of them.

def max_of_three():
	num1 = raw_input("First number: ")
	num2 = raw_input("Second number: ")
	num3 = raw_input("Third number: ")
	print "Highest number is", max (num1, num2, num3)

#Define a function that computes the length of a given string.

def count_string():
	print "Write whatever you want here"
	string_length = raw_input("")

	print "Number of characters in your sentence", len(string_length)

#Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def check_vowel():

	user_letter = raw_input("enter a letter: ")

	vowels = ['a', 'e', 'i', 'o', 'u']

	if user_letter.lower() in vowels:
		print "This is a vowel"
	else:
		print "This is not a vowel"

count_string()		
max_of_three()
check_vowel()