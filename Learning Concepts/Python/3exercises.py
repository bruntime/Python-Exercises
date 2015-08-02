#Define a function max_of_three() that takes three numbers and returns the largest of them.

def max_of_three():

#with max() function

	num1 = raw_input("First number: ")
	num2 = raw_input("Second number: ")
	num3 = raw_input("Third number: ")
	print "Highest number is", max (num1, num2, num3)

#without max() function	

	numbers = []
	
	new_num1 = raw_input("First number: ")
	numbers.append(new_num1)
	new_num2 = raw_input("Second number: ")
	numbers.append(new_num2)
	new_num3 = raw_input("Third number: ")
	numbers.append(new_num3)

	numbers = [int(x) for x in numbers]
	numbers.sort()
	
	print numbers[-1]

#Define a function that computes the length of a given string.

def count_string():

#with len() function

	print "Write something here"
	string1 = raw_input("")

	print "Number of characters in this 1st sentence", len(string1)
	
#without using the built in len() function
	
	print "Write more here"
		
	string2 = raw_input("")
	
	str_length = 0
	
	for x in string2:
		str_length += 1

	print "Number of characters in this 2nd sentence", str_length
		
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