# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum. 

def lone_sum(x, y, z):

	nums = []
	nums.append(x)
	nums.append(y)
	nums.append(z)

	print nums
	
	num_set = (set(nums))
	
	print num_set

	sum = 0
	
	for x in num_set:
		sum += int(x)
	
	print sum
	
num1 = raw_input("Number 1: ")
num2 = raw_input("Number 2: ")
num3 = raw_input("Number 3: ")
	
lone_sum(num1, num2, num3)