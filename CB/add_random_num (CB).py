# Program Name: Simple Adding
# Task Description: have the function SimpleAdding(num) add up all the numbers from 1 to a given number.
# Parameter: Accepts any number from 1 to 1000
# Example: N/A

def SimpleAdding(num):

	sum = 0
	
	#add all numbers and return sum
	for i in range(1, num+1):
		sum += i
		print sum

user_num = int(raw_input("Pick a number: "))

SimpleAdding(user_num)

#http://www.coderbyte.com/CodingArea/Editor.php?ct=Simple%20Adding&lan=Python