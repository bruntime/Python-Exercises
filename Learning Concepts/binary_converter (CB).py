#BinaryConverter

#decimal form of the binary value, binary value to decimal form. 
#Example: if 101 is passed return 5, or if 1000 is passed return 8.

import math

def decimal_converter(num):
		
	binary_nums = list(num)
	binary_convert = []
	
#index 0
	if binary_nums[0] == "1":
		place_0 = pow(2, 7)
		binary_convert = binary_convert + [place_0]
	elif binary_nums[0] == "0":
		zero = 0
		binary_convert = binary_convert + [zero]

#index 1
	if binary_nums[1] == "1":
		place_1 = pow(2, 6)
		binary_convert = binary_convert + [place_1]
	elif binary_nums[1] == "0":
		zero = 0
		binary_convert = binary_convert + [zero]

#index 2
	if binary_nums[2] == "1":
		place_2 = pow(2, 5)
		binary_convert = binary_convert + [place_2]
	elif binary_nums[2] == "0":
		zero = 0
		binary_convert = binary_convert + [zero]

#index 3
	if binary_nums[3] == "1":
		place_3 = pow(2, 4)
		binary_convert = binary_convert + [place_3]
	elif binary_nums[3] == "0":
		zero = 0
		binary_convert = binary_convert + [zero]

#index 4
	if binary_nums[4] == "1":
		place_4 = pow(2, 3)
		binary_convert = binary_convert + [place_4]
	elif binary_nums[4] == "0":
		zero = 0
		binary_convert = binary_convert + [zero]		

#index 5
	if binary_nums[5] == "1":
		place_5 = pow(2, 2)
		binary_convert = binary_convert + [place_5]
	elif binary_nums[1] == "0":
		zero = 0
		binary_convert = binary_convert + [zero]
		
#index 6
	if binary_nums[6] == "1":
		place_6 = pow(2, 1)
		binary_convert = binary_convert + [place_6]
	elif binary_nums[6] == "0":
		zero = 0
		binary_convert = binary_convert + [zero]		
		
#index 7
	if binary_nums[7] == "1":
		place_7 = pow(2, 0)
		binary_convert = binary_convert + [place_7]
	elif binary_nums[7] == "0":
		zero = 0
		binary_convert = binary_convert + [zero]
		
	print binary_convert
	print sum(binary_convert)
		
binary_num = raw_input("Number (no more than 8 characters): ") [:8]#maximum user input (8 characters)
decimal_converter(binary_num)