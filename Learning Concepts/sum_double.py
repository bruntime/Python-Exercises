#Exercise: Sum and Double

def sum_double (a, b):

	sum = a + b

	if a == b:
		print sum * 2
	else:
		print sum
	
num1 = int(raw_input("Enter first number: "))	
num2 = int(raw_input("Enter second number: "))	
sum_double(num1, num2)