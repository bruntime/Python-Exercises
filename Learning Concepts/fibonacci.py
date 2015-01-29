#Project: Fibonacci Sequence

list_of_nums = [1, 2]

a = 0
b = 1

while b < 10:

	a += 1
	b += 1
	
#Expected Result: Sum = number in index a + number in index b
#Actual Result: Sum = list index a + list index b, Error

	sum = list_of_nums.index(a) + list_of_nums.index(b)
	
	list_of_nums.append(sum)
	print list_of_nums
