 # take an array of integers and return the minimum number of integers needed to make the contents consecutive from the lowest number to the highest number. 
 # Example: For [4, 8, 6] the output should be 2 because two numbers need to be added to the array (5 and 7) to make it from 4 to 8. 
 # Negative numbers may be entered as parameters and no array will have less than 2 elements.
 
def consecutive(arr):
 
	nums = arr
	missing_nums = []

	for j in range(nums[0], nums[-1]+1):
		missing_nums = missing_nums +[j]
	 
	group1 = set(nums)
	group2 = set(missing_nums)
	 
	print group1, "\n", group2

	missing = group2.difference(group1)

	print "Total numbers needed to make list consecutive: ", len(missing)
 
user_nums = raw_input("Give a list of numbers: ")
numbers = map(int, user_nums.split(','))

consecutive(numbers)