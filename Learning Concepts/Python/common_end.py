# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more. 

#test
num_set1 = [1, 2, 4, 3]
num_set2 = [7, 4, 3]

if num_set1[-1] == num_set2[-1]:
	print "true"
else:
	print "false"

#using user input	
user_num_set1 = []
user_num_set2 = []

while len(user_num_set1) < 5:
	txt = int(raw_input("first set of numbers: "))
	user_num_set1 = user_num_set1 + [txt]

while len(user_num_set2) < 5:
	txt = int(raw_input("second set of numbers: "))
	user_num_set2 = user_num_set2 + [txt]

if user_num_set1[-1] == user_num_set2[-1]:
	print "true"
else:
	print "false"
