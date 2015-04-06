# Return the nth prime number
# Example: if num is 16 the output should be 53 as 53 is the 16th prime number

def prime_pick(n):

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
		
user_num = int(raw_input("nth number: "))

list_num = []	

for num in xrange (1, 10000):
	if prime_pick(num):
		list_num = list_num + [num]

print list_num[user_num-1]