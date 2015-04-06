# Return the nth prime number
# Example: if num is 16 the output should be 53 as 53 is the 16th prime number

def prime_pick(num):

	prime = []
	prime_total = len(prime)
	a = 0
	while len(prime) != 10:
		a += 1
		if num % a == 0:
		 prime = prime + [a]
	if len(prime) > 2:
		return False
	else:
		return True
	
	print prime
	
user_num = int(raw_input("nth prime pick: "))	

prime_pick(user_num)