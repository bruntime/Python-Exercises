# Program Name: Dash Between Two Odd Numbers
# Task Description:  Insert dashes ('-') between two odd numbers in string.
# Parameter: Don't count zero as an odd number.
# Example: If string is 454793 the output should be 4547-9-3.

def dash_insert(txt):

	numbers = list(txt)
	odd_numbers = [1, 3, 5, 7, 9]
	print numbers
	
	a = -1
	b = -1
	
	new_numbers = []
	
	for x in numbers:
		a +=1
		b +=1
		
		#check if first AND second numbers are odd numbers
		if numbers[a] and numbers[b] in odd_numbers:
		#if odd numbers, place dash between and save to new list
			new_numbers = new_numbers + numbers[a] + '-' + numbers[b]
			print new_numbers
	
user_txt = raw_input("Numbers: ")
dash_insert(user_txt)
