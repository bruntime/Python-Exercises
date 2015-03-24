 # have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
 #If there are two or more words that are the same length, return the first word from the string with that length. 
 #Ignore punctuation and assume sen will not be empty.
 
import string
 
user_text = raw_input("Your 3-word sentence here (punctuation accepted): ")

#1. remove punctuation marks
for x in string.punctuation:
	user_text = user_text.replace(x, "")

#2. place user text in list and separate text into words	
sentence = user_text.split(" ")

#3. keep version of list
oldsentence = sentence

#4. compare length of each word

while len(sentence) != 1: #loops until only 1 word left
	if len(sentence[0]) >= len(sentence[1]):
		sentence.remove(sentence[1])
	elif len(sentence[0]) < len(sentence[1]):
		sentence.remove(sentence[0])

print sentence