#Project Euler

#Problem #10 Summation of Primes

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def is_prime(n):
	
	prime = []
	
	a = 0
	while a <= n:
		a += 1
		if n % a == 0:
		 prime.append(a)
	if len(prime) > 2:
		return False
	else:
		return True

list_num1 = []	
list_num2 = []
list_num3 = []
list_num4 = []

for num in xrange (1, 500000):
	if is_prime(num):
		list_num1 = list_num1 + [num]
		
for num in xrange (500000, 1000000):
	if is_prime(num):
		list_num2 = list_num2 + [num]

for num in xrange (1000000, 1500000):
	if is_prime(num):
		list_num3 = list_num3 + [num]

for num in xrange (1500000, 2000000):
	if is_prime(num):
		list_num4 = list_num4 + [num]	
		
print sum(list_num1 + list_num2 + list_num3 + list_num4)