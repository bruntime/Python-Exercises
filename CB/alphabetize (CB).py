#Return a string with the letters in alphabetical order (ie. hello becomes ehllo). 
#Assume numbers and punctuation symbols will not be included in the string.

def string_alphabetical_order(word):

	word = "".join(c for c in word if c not in ('!','.',':', '?', '"', '(', ')', '^', '&', '?', '`', '~'))

	chars = list(word)
	print chars	
	chars.sort()
	
	characters = []
	
	characters = "".join(x for x in chars)
	print characters
		
one_word = raw_input("Write word here: ")

string_alphabetical_order(one_word)