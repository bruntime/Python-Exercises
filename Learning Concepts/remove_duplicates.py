# Write a program that accepts a list of elements from the user and then print the list after removing all duplicate values, preserving the original order.

user_max = int(raw_input("Size of list: "))

#use a set to remove duplicates of numbers in list
new_nums = set( )

while len(new_nums) < user_max:
	num = int(raw_input("number: "))
	new_nums.add(num)
	
#order numbers
	
print new_nums