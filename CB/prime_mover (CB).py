# Return the nth prime number
# Example: if num is 16 the output should be 53 as 53 is the 16th prime number

def prime_pick(num):

	prime = []
	
	a = 0
	while a <= num:
		a += 1
		if num % a == 0:
		 prime = prime + [a]
	if len(prime) > 2:
		return False
	else:
		return True
		
num = int(raw_input("nth prime pick: "))	
count = []
x = 1

while len(count) < num+1:
	x += 1
	if prime_pick(x):
		count = count + [x]
	print count[-1]