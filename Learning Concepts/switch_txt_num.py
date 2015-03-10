#Learn how to implement a dictionary
#a = 1, b = 2, c = 3, d = 4, .... y = 25, z = 26 

def txt_num(char):

	d = dict()
	
	for c in char:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	print d
	
txt = raw_input("Characters: ")
chars = list(txt)

txt_num(chars)

#http://www.greenteapress.com/thinkpython/html/thinkpython012.html