# Have the function ExOh(str) take the str parameter being passed and return the string true if there is an equal number of x's and o's.
# Otherwise return the string false. 
# Only these two letters will be entered in the string, no punctuation or numbers. 
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

def ExOh(str):
	
	count_x = str.count('x')
	count_o = str.count('o')
	
	print count_o
	print count_x
	
	if count_o == count_x:
		print 'true'
	else:
		print 'false'
		
txt = raw_input("input as many x's and o's as you'd like - x's and o's only: ")

ExOh(txt) 

#CoderByte exercise: http://coderbyte.com/CodingArea/Challenges/