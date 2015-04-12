# Take an array of strings and return the third largest word within in. 
# The array will have at least three strings and each string will only contain letters. 

def third_longest(list_words):

	for x in list_words:
	# determine which x is longest

user_list_words = []
user_txt = 0

count = 0
while user_txt != 'done':
	count +=1
	user_txt = raw_input("A word: ")
	if count < 3:
		print "You have to input  %d words" %(3 - count)

third_longest(user_list_words)