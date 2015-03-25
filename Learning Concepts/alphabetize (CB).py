#Return a string with the letters in alphabetical order (ie. hello becomes ehllo). 
#Assume numbers and punctuation symbols will not be included in the string.

def string_alphabetical_order(word):

	chars = list(word)
	print chars	
	chars.sort()
	print chars

one_word = raw_input("Write word here: ")

string_alphabetical_order(one_word)