#Divide number by two to make a new number.
#example: 100, the screen output should be - 100, 50, 25, 12.5 ....

def half(num):

	nums = []
	
	while num > 0.02:
		nums.append(num)
		num = num/2
	print nums

user_num = float(raw_input("number: "))
half(user_num)