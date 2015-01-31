#Project Euler

#Problem #3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

a = 0
num = 1

factors = []
prime_nums = []

while a < (600851475143/2):
	a += 1
	if 600851475143 % a == 0:
		factors.append(a)
print factors

for x in factors:
	while num < 10:
		num += 1
		if x % num != 0: #checks which numbers in list are prime
			prime_nums.append(x) #error: appends list with ones
print prime_nums



