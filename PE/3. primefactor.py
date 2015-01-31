#Project Euler

#Problem #3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

a = 0

factors = []

while a < (600851475143/2):
	a += 1
	if 600851475143 % a == 0:
		factors.append(a)

print factors #need to determine if factors are prime

# prime_nums = []

# for x in factors:
	# if x % ___ != 0:
		# prime_nums.append(x)



