# have the function SimpleAdding(num) add up all the numbers from 1 to num. For the test cases, the parameter num will be any number from 1 to 1000. 

def SimpleAdding(num):

	sum = 0
	
	for i in range(1, num):
		sum += i
	print sum

end_num = int(raw_input("Pick a number: "))

SimpleAdding(end_num)

