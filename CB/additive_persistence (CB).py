# Program Name: Additive Persistence
# Task Description: Return a number's additive persistence which is the number of times you must add the digits until you reach a single digit. 
# Parameter: N/A
# Example: If num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9

def Add_Persist(num):

	num_list = []
	num_list.append(num)
	
	while len(num_list) > 1: #iterate until only one number left in list
		for [int(x) for x in str(num)]: #iterate through numbers as a string, then convert back to integer
			sum_digits = sum(num_list) #add numbers in list
		del num_list[:] #clear empty list
		num_list.append(sum_digits) #add new numbers to list
		print num_list
	
number = int(raw_input("Give me a number: "))

Add_Persist(number)

#http://www.coderbyte.com/CodingArea/Editor.php?ct=Additive%20Persistence&lan=Python