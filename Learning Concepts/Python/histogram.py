# Program Name: Histogram
# Task Description: Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# Parameter: N/A
# Example: histogram([4, 9, 7]) should print the following:

# ****
# *********
# ******* 

def histogram(num):

	num_list = []
	num_list = num
	del num_list[-1]
	
	print num_list
	
	for x in num_list:
		print "*" * int(x)

user_num= 0
user_num_list = []

print "When complete, type 'done' to end"
while user_num != 'done':
	user_num = raw_input("How many stars? ")
	user_num_list.append(user_num)
histogram(user_num_list)