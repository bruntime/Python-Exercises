# Program Name: Pangram or Not
# Task Description: Check a sentence to see if it a pangram. (A pangram is a sentence that contains all the letters of the English alphabet at least once)
# Parameter: N/A
# Example: The quick brown fox jumps over the lazy dog.
# Note: Problem 18

def pangram(sentence):

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	# characters = [x for x in sentence.split()]
	
	if all ((x in letters) for x in sentence):
		print "Is a pangram"
	else:
		print "Not a pangram"
	
user_txt = raw_input("Sentence: ")
pangram(user_txt)

#http://www.ling.gu.se/~lager/python_exercises.html