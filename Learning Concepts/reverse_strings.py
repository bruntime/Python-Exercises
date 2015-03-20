#Reverse Input - program that reads strings input and prints them in reverse order
# Example:
# one
# two
# three
# Prints as:
# three
# two
# one

def reversing_txt(user_input):

	user_input.remove('done')
	for x in reversed(user_input):
		print x
	
print "Type done when complete"

txt = 0
count = 0

all_txt = []

while txt != 'done':
	count += 1
	txt = raw_input("What would you like to say? ")
	all_txt = all_txt + [txt]
	
reversing_txt(all_txt)