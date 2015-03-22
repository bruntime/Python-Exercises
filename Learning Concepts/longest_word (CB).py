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
for x in sentence:
	print len(x)