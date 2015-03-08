#BinaryConverter

#decimal form of the binary value, binary value to decimal form. 
#Example: if 101 is passed return 5, or if 1000 is passed return 8.

import math

def decimal_converter(num):
		
	binary_nums = list(num)
	binary_convert = []
	zero = 0

#index 0
	if binary_nums[0] == "1":
		place_0 = pow(2, 7)
		binary_convert = binary_convert + [place_0]
	elif binary_nums[0] == "0":
		binary_convert = binary_convert + [zero]

#index 1
	if binary_nums[1] == "1":
		place_1 = pow(2, 6)
		binary_convert = binary_convert + [place_1]
	elif binary_nums[1] == "0":
		binary_convert = binary_convert + [zero]

#index 2
	if binary_nums[2] == "1":
		place_2 = pow(2, 5)
		binary_convert = binary_convert + [place_2]
	elif binary_nums[2] == "0":
		binary_convert = binary_convert + [zero]

#index 3
	if binary_nums[3] == "1":
		place_3 = pow(2, 4)
		binary_convert = binary_convert + [place_3]
	elif binary_nums[3] == "0":
		binary_convert = binary_convert + [zero]

#index 4
	if binary_nums[4] == "1":
		place_4 = pow(2, 3)
		binary_convert = binary_convert + [place_4]
	elif binary_nums[4] == "0":
		binary_convert = binary_convert + [zero]		

#index 5
	if binary_nums[5] == "1":
		place_5 = pow(2, 2)
		binary_convert = binary_convert + [place_5]
	elif binary_nums[1] == "0":
		binary_convert = binary_convert + [zero]
		
#index 6
	if binary_nums[6] == "1":
		place_6 = pow(2, 1)
		binary_convert = binary_convert + [place_6]
	elif binary_nums[6] == "0":
		binary_convert = binary_convert + [zero]		
		
#index 7
	if binary_nums[7] == "1":
		place_7 = pow(2, 0)
		binary_convert = binary_convert + [place_7]
	elif binary_nums[7] == "0":
		binary_convert = binary_convert + [zero]
		
	print binary_convert
	print sum(binary_convert)
	
def binary_converter(num):

	decimal_convert = []
	zero = 0

	if num >= pow(2, 7):
		place_0 = 1
		decimal_convert = decimal_convert + [place_0]
		num = num - pow(2, 7)
	else:
		decimal_convert = decimal_convert + [zero]
	
	if num >= pow(2,6):
		place_1 = 1
		decimal_convert = decimal_convert + [place_1]
		num = num - pow(2,6)
	else:
		decimal_convert = decimal_convert + [zero]

	if num >= pow(2,5):
		place_2 = 1
		decimal_convert = decimal_convert + [place_2]
		num = num - pow(2,5)
	else:
		decimal_convert = decimal_convert + [zero]
		
	if num >= pow(2,4):
		place_3 = 1
		decimal_convert = decimal_convert + [place_3]
		num = num - pow(2,4)
	else:
		decimal_convert = decimal_convert + [zero]
		
	if num >= pow(2,3):
		place_4 = 1
		decimal_convert = decimal_convert + [place_4]
		num = num - pow(2,3)
	else:
		decimal_convert = decimal_convert + [zero]

	if num >= pow(2,2):
		place_5 = 1
		decimal_convert = decimal_convert + [place_5]
		num = num - pow(2,2)
	else:
		decimal_convert = decimal_convert + [zero]

	if num >= pow(2,1):
		place_6 = 1
		decimal_convert = decimal_convert + [place_6]
		num = num - pow(2,1)
	else:
		decimal_convert = decimal_convert + [zero]

	if num >= pow(2,0):
		place_7 = 1
		decimal_convert = decimal_convert + [place_7]
		num = num - pow(2,0)
	else:
		decimal_convert = decimal_convert + [zero]				
		
	print decimal_convert

print "Conversion from Binary to Decimal or Decimal to Binary"
choice = raw_input("Convert to: Binary or Decimal? ")

if choice == "Binary" or choice == "binary":
	binary_num = raw_input("Please input a binary number (no more than 8 characters): ") [:8]#maximum user input (8 characters)
	decimal_converter(binary_num)

if choice == "Decimal" or choice == "decimal":
	decimal_num =int(raw_input("Please input a number (less than 255): "))
	binary_converter(decimal_num)