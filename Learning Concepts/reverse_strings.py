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

	all_txt = []
	
	all_txt = all_txt + [user_input]

print "Type done when complete"

txt = raw_input("What would you like to say? ")

while txt != 'done':
	print reversing_txt(txt)
	