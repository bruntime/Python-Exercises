# Search for all the numbers in the string, add them together, then return that final number. 
# For example: if str is "88Hello 3World!" the output should be 91. 
# You will have to differentiate between single digit numbers and multiple digit numbers like in the example above. 
# So "55Hello" and "5Hello 5" should return two different answers. 
# Each string will contain at least one letter or symbol. 

def number_search(txt):

	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	
	characters = []
	characters = txt.split(" ")
	
	numbers_from_txt = []
	
	a = 0
	
	for x in characters:
		if x == a in numbers:
			print x

sentence = raw_input("Sentence here (with numbers): ")

number_search(sentence)