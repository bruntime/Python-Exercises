# Search for all the numbers in the string, add them together, then return that final number. 
# For example: if str is "88Hello 3World!" the output should be 91. 
# You will have to differentiate between single digit numbers and multiple digit numbers like in the example above. 
# So "55Hello" and "5Hello 5" should return two different answers. 
# Each string will contain at least one letter or symbol. 

def number_search(txt):

	characters = list(txt)
	
	print characters
	
	numbers_from_txt = []
	
	for x in characters:
		if x == '1' or x == '2' or x == '3'or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0':
			numbers_from_txt.append(int(x))
	print numbers_from_txt
	print sum(numbers_from_txt)

sentence = raw_input("Sentence here (with numbers): ")

number_search(sentence)