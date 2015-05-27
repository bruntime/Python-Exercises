# Program Name: Array Addition
# Task Description: Take array of numbers and return the string true if any combination of numbers in the array can be added up to equal the largest number in the array, otherwise return the string false.
# Parameter: The array will not be empty, will not contain all the same elements, and may contain negative numbers.
# Example: If arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. 

def addition(arr):

	numbers = arr
	numbers.sort()
	print numbers
	
	sum_arr = sum(numbers)
	print sum_arr
	
user_txt = list(input("Numbers: "))
addition(user_txt)