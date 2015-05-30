def simplesymbols(str):

	txt = list(str)
	print txt
	
	x = '+'
	y = '='
	
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	
	for y in alphabet:
		if y in txt:
			print 'true'

user_txt = raw_input("String: ")
simplesymbols(user_txt)