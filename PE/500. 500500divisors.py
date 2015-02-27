#Project Euler

#Problem #500

#The number of divisors of 120 is 16.
#In fact 120 is the smallest number having 16 divisors.

#Find the smallest number with 2^500500 divisors.
#Give your answer modulo 500500507.

divisor = 0
factors = []
num = (len(factors)== 500)

for x in range(1, num):
	while x < num:
		divisor += 1
		while divisor <= num:
			if num % divisor == 0:
				factors.append(divisor)
			elif num % divisor != 0:
				break
			
print (factors)