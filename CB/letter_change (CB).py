# Program Name: Letter Change
# Task Description: Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
# Parameter: N/A
# Example: "fun times" becomes "gvO Ujnft!"

import string

def letter_change(str):

	sentence = list(str)
	print (sentence)
	
	letters = list(string.ascii_lowercase)
	print (letters)
	
	for x in sentence: 

user_input = input("Sentence: ").lower
letter_change(user_input)

#http://coderbyte.com/CodingArea/Editor.php?ct=Letter%20Changes&lan=Python