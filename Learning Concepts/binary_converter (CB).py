#BinaryConverter

#decimal form of the binary value, binary value to decimal form. 
#Example: if 101 is passed return 5, or if 1000 is passed return 8.

import math

binary_nums = []

def binary_converter(num):

	power_2 = 0
	
	while power_2 > 0:
		power_2 = num/2
		binary_nums.append(power_2)

#function binary to decimal converter
# def decimal_converter(num):
		
decimal_num = int(raw_input("Number: "))
binary_num = int(raw_input("Number: "))

binary_converter(decimal_num)
decimal_converter(binary_num)
	
	
