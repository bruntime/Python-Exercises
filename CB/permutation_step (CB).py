# Program Name: Scrambled Numbers
# Task Description:  Take the numbers being passed and return the next number greater than given number using the same digits. If a number has no greater permutations, return -1 (ie. 999). 
# Parameter: N/A
# Example: If num is 123 return 132, if it's 12453 return 12534.

import itertools

def permutation(num):

	numbers = list(num)
	print (numbers)
	
user_txt = input("Number: ")
permutation(user_txt)