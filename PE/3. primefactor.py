#Project Euler

#Problem #3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

a = 1
check_num = 2000
factors = []
prime_num = []

while a <= check_num:
	a +=1
	if check_num % a == 0:
		factors.append(a)
print factors

i = 0

x for x in factors:
	while i != factors[-1]:
		i += 1
		if (x / i) == 1:
			prime_num.append(x)		
print prime_num

