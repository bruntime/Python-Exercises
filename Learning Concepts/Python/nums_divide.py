def lower_nums():
	
	user_num = int(raw_input("Pick a number: "))
	
	x = 0
	nums = []
	
	while x < user_num:
	
		x += 1
		if x % 2 == 0  and x % 3 == 0:
			print x, "divisible by both"
			nums.append(x)			
		elif x % 2 == 0:
			print x, "divisible by 2"
		elif x % 3 == 0:
			print x, "divisible by 3"
			
	print "By both", nums
	
lower_nums()