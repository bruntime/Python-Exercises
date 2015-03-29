def LetterCount(txt):

	word =[]
	word = txt.split(" ")
	
	#sort characters in word
	
	char_list = list(word[0])
	print char_list
	char_list.sort()
	print char_list
	
	letters = {'a': 0,  'b': 0,  'c': 0,  'd': 0,  'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
	
	count = 0
	
	#update dictionary with letter count
	for x in char_list:
		if x == letters['a']:
			count += 1
			letters['a'] = count
			print count
	
user_txt = raw_input("sentence: ")

LetterCount(user_txt)