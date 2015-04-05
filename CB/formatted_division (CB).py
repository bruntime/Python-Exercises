# FormattedDivision(num1,num2) take both parameters being passed, divide num1 by num2.
# Return the result as a string with properly formatted commas and 4 significant digits after the decimal place. 
# For example: if num1 is 123456789 and num2 is 10000 the output should be "12,345.6789". 
# The output must contain a number in the one's place even if it is a zero.

import string

def format_division(num1, num2):

	print("{:8,.4f}".format(float(num1)/float(num2)))

user_num1 = int(raw_input("Number 1: ")) 
user_num2 = int(raw_input("Number 2: "))

format_division(user_num1, user_num2)