# LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space

def letter_capitalize(str):

	sentence = str.split(" ")
	
	sentence = [x.capitalize() for x in sentence]
	
	for x in sentence:
		print x 

user_txt = raw_input("Sentence here: ")

letter_capitalize(user_txt)