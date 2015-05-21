# Program Name: Letter Change
# Task Description: Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
# Parameter: N/A
# Example: "fun times" becomes "gvO Ujnft!"

import string

def letter_change(str):

	sentence = list(str)
	print (sentence)
	
	alphabet = list(string.ascii_lowercase)
	print (alphabet)
	
	letters = {}
	
	a = 0 #for elements in alphabet list
	b = 1 #for dictionary value
	
	while  a<= alphabet[-1]:
		a += 1
		b += 1
		#add keys and corresponding values to the dictionary
		letters[alphabet[a]] = b
	print (letters)
	
user_txt = input("Sentence: ").lower()
letter_change(user_txt)

#http://coderbyte.com/CodingArea/Editor.php?ct=Letter%20Changes&lan=Python