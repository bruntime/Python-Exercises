# Have the function ExOh(str) take the str parameter being passed and return the string true if there is an equal number of x's and o's.
# Otherwise return the string false. 
# Only these two letters will be entered in the string, no punctuation or numbers. 
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

def ExOh(str):

	count_x = 0
	count_o = 0
	
	count_xo = str

	for i in list(count_xo):
		if i == 'x':
			count_x += 1
		elif i == 'o':
			count_o += 1
		else:
			return
	
	print count_o
	print count_x
	
	if count_o == count_x:
		print 'true'
	else:
		print 'false'
		
txt = raw_input("input as many x's and o's as you'd like - x's and o's only: ")

ExOh(txt) 

#CoderByte exercise: http://coderbyte.com/CodingArea/Challenges/