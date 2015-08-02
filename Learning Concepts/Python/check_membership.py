# Program Name: Check Membership
# Task Description Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. 
#Parameter: Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.
#Example: N/A

def is_member( value_check, values_list):

	list_to_check = values_list
	value_to_check = value_check
	
	count = -1
	
	while count != len(list_to_check):
		count += 1
		if value_to_check != list_to_check[count]:
			print "False"
		else:
			print "True"
	
user_list = []
user_input = 0

print "Type 'done' to end list input"

while user_input != 'done':
	user_input = raw_input("List values: ")
	user_list.append(user_input)
	
check_value = raw_input("What value to check? ")

is_member( user_list, check_value)

	