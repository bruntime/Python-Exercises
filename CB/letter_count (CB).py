# Program Name: Letter Count
# Task Description:  Return the first word with the greatest number of repeated letters. If there are no words with repeating letters return -1.
# Parameter: Words will be separated by spaces.
# Example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's.

def LetterCount(txt):

	sentence = txt.split(" ")
	sentence = [x.lower() for x in sentence]
	print sentence
	
	#separate characters in each word and place each set of characters in a list
	characters = [list(x) for x in sentence]
	print characters
	
	count = 0
	
	#find repeating characters in each set
	for y in characters:
			
user_txt = raw_input("sentence: ")

LetterCount(user_txt)

#http://coderbyte.com/CodingArea/Editor.php?ct=Letter%20Count&lan=Python