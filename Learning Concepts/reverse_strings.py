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

	for x in reversed(all_txt):
		print x
	
print "Type done when complete"

count = 0

all_txt = []

while count < 10:
	count += 1
	txt = raw_input("What would you like to say? ")
	all_txt = all_txt + [txt]
	
reversing_txt(all_txt)