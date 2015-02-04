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

list_num = []	
		
for num in range (2, 2000000):
	if is_prime(num):
		list_num = list_num + [num]
print sum(list_num)