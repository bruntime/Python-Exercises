# Return a number's additive persistence which is the number of times you must add the digits until you reach a single digit. 
# For example: if num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9

def Add_Persist(num):

	num_list = [int(i) for i in str(num)]

	while len(num_list) > 1:
		sum_digits = sum(num_list)
		num_list.append(sum_digits)
		print sum(num_list)
	
number = int(raw_input("Give me a number: "))

Add_Persist(number)