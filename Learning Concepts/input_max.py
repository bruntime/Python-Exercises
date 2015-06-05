#Description: accept strings as input until there are 15 strings accepted or user input is empty 

#If input contains digits (0 -9) display the sum of digits and ignore the other characters
#If input is palindrome display the string "palindrome", otherwise print the input in reverse order (case sensitive)

txt = []
numbers_in_txt = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



while len(txt) != 15:
	user_txt = raw_input("Test: ")
	txt = txt + [user_txt]
	if user_txt == "":
		txt.pop()
		break
	
	# numbers_in_txt = []

	# for x in list(user_txt):
		# if x in numbers:
			# numbers_in_txt.append(int(x))
	# print sum(numbers_in_txt)		
		
	# if user_txt == "":
		# break
	# else:
		# txt = txt + [user_txt]	

print txt
print "There were",  len(txt), "input(s)"