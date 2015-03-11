#Learn how to implement a dictionary
#a = 1, b = 2, c = 3, d = 4, .... y = 25, z = 26 

def txt_num(char):

	letters = {
	'a': 1, 
	'b': 2, 
	'c': 3, 
	'd': 4, 
	'e': 5,
	'f': 6,
	'g': 7,
	'h': 8,
	'i': 9,
	'j': 10,
	'k': 11,
	'l': 12,
	'm': 13,
	'n': 14,
	'o': 15,
	'p':16,
	'q':17,
	'r':18,
	's':19,
	't':20,
	'u':21,
	'v':22,
	'w':23,
	'x':24,
	'y':25,
	'z':26}
	
	user_txt = list(char)
	
	print user_txt
	
	# letter_switch = []
	
	for x in user_txt:
		print letters[x]
		
		#add x to letter_switch list

txt = raw_input("Characters: ")

txt_num(txt)

#http://www.greenteapress.com/thinkpython/html/thinkpython012.html