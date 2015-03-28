def LetterCount(txt):

	word =[]
	word = txt.split(" ")
	
	#sort characters in word
	
	char_list = list(word[0])
	print char_list
	char_list.sort()
	print char_list
	
	# a = -1
	# b = 0
	# count = 0
	
	#compare each character in a word
	#count how many times a specific character shows up in the word
	#if one character shows up more times than another, print count and character
	
	# while count < char_list[-1]:
		# if char_list[a] == char_list[b]:
			# a += 1
			# b += 1
			# count += 1
			# print count
		# else:
			# return
	
user_txt = raw_input("sentence: ")

LetterCount(user_txt)