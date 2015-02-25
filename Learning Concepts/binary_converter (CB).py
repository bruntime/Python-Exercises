#BinaryConverter

#decimal form of the binary value, binary value to decimal form. 
#Example: if 101 is passed return 5, or if 1000 is passed return 8.

import math

def decimal_converter(num):
		
	binary_nums = list(num)
	binary_convert = []
	
	for x in binary_nums:
			print x
			print binary_nums
		
	if binary_nums[0] == "1":
		place_0 = pow(2, 8)
		print place_0
	elif binary_nums[0] == "0":
		print "0"
	
	
	if binary_nums[1] == "1":
		place_1 = pow(2, 7)
		print place_1
	elif binary_nums[1] == "0":
		print "0"
		
binary_num = raw_input("Number (no more than 8 characters): ") [:8]#maximum user input (8 characters)
decimal_converter(binary_num)
