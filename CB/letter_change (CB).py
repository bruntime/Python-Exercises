# Program Name: Letter Change
# Task Description: Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
# Parameter: N/A
# Example: "fun times" becomes "gvO Ujnft!"

import string

def letter_change(str):

	sentence = str.replace(' ', '')
	sentence = list(str)
	print (sentence)

	letters = {'a': 'b',  'b': 'c',  'c': 'd',  'd': 'e',  'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
	
	changed_txt = []
	
	#replace letters with corresponding value
	for x in sentence:
		changed_txt = changed_txt + [letters[x]]
	
	#capitalize vowels
	for y in changed_txt:
		if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u':	
			changed_txt[changed_txt.index(y)] = y.upper()

	# changed_txt = ''.join([str(x) for x in changed_txt])
	
	print (changed_txt)
			
user_txt = input("Sentence: ").lower()
letter_change(user_txt)

#http://coderbyte.com/CodingArea/Editor.php?ct=Letter%20Changes&lan=Python