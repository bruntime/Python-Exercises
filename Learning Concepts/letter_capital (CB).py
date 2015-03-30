# LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space

def letter_capitalize(str):

	sentence = str.split(" ")
	
	for x in sentence:
		word = x.capitalize()
		print x

user_txt = raw_input("Sentence here: ")

letter_capitalize(user_txt)