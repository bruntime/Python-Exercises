# Write a function/method to find an integer from the array who equals to its index. 
# For example, in the array {-3, -1, 1, 3, 5}, the number 3 equals its index 3.

num_lists = [-3, -1, 1, 3, 5]

a = 0

for x in num_lists:
	a += 1
	if x == num_lists.index(a):
		print x
