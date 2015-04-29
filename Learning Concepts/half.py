#Divide number by two to make a new number.
#example: 100, the screen output should be - 100, 50, 25, 12.5 ....

def half(num):

	nums = []
	
	while num > 0.5:
		nums.append(num)
		num = num/2
	
	#print on separate lines
	for x in nums:
		print x
	
	print '*' * 80
	
	# print without list brackets (converts float to string)
	print ', '.join(map(str, nums))

user_num = float(raw_input("number: "))
half(user_num)