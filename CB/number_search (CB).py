from decimal import decimal

def NumberSearch(str): 

  	str = "".join(c for c in str if c not in ('!','.',':', '?', '"', '(', ')', '^', '&', '?', '`', '~', ' ', ','))
	
	characters = list(str)
	letters = list(c for c in str if c not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
	
	print characters
	print letters
	
	numbers_from_txt = []
	
	for x in characters:
		if x == '1' or x == '2' or x == '3'or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0':
			numbers_from_txt.append(int(x))
	print sum(numbers_from_txt)
	print len(characters)
	print decimal(sum(numbers_from_txt)/len(letters))
    
user_txt = raw_input('sentence: ')

NumberSearch(user_txt)
