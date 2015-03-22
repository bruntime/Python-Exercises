 # have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
 #If there are two or more words that are the same length, return the first word from the string with that length. 
 #Ignore punctuation and assume sen will not be empty.
 
import string
 
user_text = raw_input("Your sentence here: ")

#1. remove punctuation marks
for x in string.punctuation:
	user_text = user_text.replace(x, "")

#2. place user text in list and separate text into words	
sentence = user_text.split(" ")
print sentence

#4. compare length of each word
#(INCOMPLETE SECTION)
#Progress: currently works with 3 words

a = 0
b = 0

if len(sentence[0]) >= len(sentence[1]):			#sentence 1: 5 char 		sentence 2: 5 char
	a = sentence[0]											#keep sentence 1
	# print a
elif len(sentence[0]) < len(sentence[1]):		#sentence 1: 4 char		sentence 2: 5 char
	a = sentence[1]											#keep sentence 2
	# print a

if len(a) >= len(sentence[-1]):
	print a
else:
	b = sentence[-1]
	print b