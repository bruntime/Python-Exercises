# Return the nth prime number
# Example: if num is 16 the output should be 53 as 53 is the 16th prime number

def prime_pick(n):

	prime = []
	
	while len(prime) != n:
		for num in range(1, 10):
			if num > 1:
				for i in range (2, num):
					if (num % i) == 0:
						break
				else:
					print (num)
		
user_num = int(raw_input("nth number: "))

prime_pick(user_num)