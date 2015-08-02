# Program Name: Pangram or Not
# Task Description: Check a sentence to see if it a pangram. (A pangram is a sentence that contains all the letters of the English alphabet at least once)
# Parameter: N/A
# Example: The quick brown fox jumps over the lazy dog.
# Note: Problem 18

def pangram(sentence):

	sentence = sentence.replace(' ', '')
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	characters = list(sentence)
	
	a = -1
	count = 0
	while letters[a] in characters:
		a += 1
		count += 1
		break
		
	if count == 26:
		print "Is a pangram"
	else:
		print "Is not a pangram"
	
user_txt = raw_input("Sentence: ").lower()
pangram(user_txt)

#http://www.ling.gu.se/~lager/python_exercises.html