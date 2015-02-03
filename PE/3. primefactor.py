#Project Euler

#Problem #3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

factors = []

def is_prime(n):
	
	a = 0
	while a <= n:
		a += 1
		if n % a == 0:
		 factors.append(a)
	if len(factors) > 2:
		return False
	else:
		return True

a = 1
check_num = 600851475143

while a <= check_num:
	a +=1
	if check_num % a == 0:
		if is_prime(a):
			factors.append(a)
print factors[-1]