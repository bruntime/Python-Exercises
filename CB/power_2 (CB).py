# Program Name: Power of 2 Checker
# Task Description: Check if an integer is a power of two. If it is return the string true. If it's not return the string false.
# Parameter: N/A
# Example: if the input is 16 then your program should return the string true but if the input is 22 then the output should be the string false.

import math

def Power_of_2(num):

	#make user input into a float for compatibility with power_check values (which are returned as float)
	user_num = float(num)
	nums = []
	
	for i in range (1, num + 1):
		power_check = (math.pow(i, 2))
		nums = nums + [power_check]
	print (nums)

	if user_num in nums:
		print ("Is a power of 2")
	else:
		print ("Is not a power of 2")
		
check_num = int(input("Check if number is power of 2: "))

Power_of_2(check_num)

#http://coderbyte.com/CodingArea/Editor.php?ct=Powers%20of%20Two&lan=Python