# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum. 

from collections import OrderedDict

def lone_sum(x, y, z):

	nums = []
	nums.append(x)
	nums.append(y)
	nums.append(z)

	print nums
	
	len(nums) != len(set(nums))
	
	print (set(nums))
	
num1 = raw_input("Number 1: ")
num2 = raw_input("Number 2: ")
num3 = raw_input("Number 3: ")
	
lone_sum(num1, num2, num3)