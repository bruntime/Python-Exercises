#take 2 strings and determine if a portion of string 1 characters can be rearranged to match sring2
# if yes return the string true, otherwise return the string false

def scramble (str1, str2):

	txt1 = list(str1)
	txt1.sort()
	
	print txt1
	
	txt2 = list(str2)
	txt2.sort()
	print txt2
	
	# a = 0
	
	for x in txt2:
		# while x == 'true':
			# a += -1
		if txt1[0] == x:
			print 'true'
		else:
			print 'false'

user_txt1 = raw_input("sentence 1: ")
user_txt2 = raw_input("sentence 2: ")

scramble(user_txt1, user_txt2)