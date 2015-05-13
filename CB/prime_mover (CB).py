# Program Name: Nth Prime Number
# Task Description:  Return the nth prime number
# Parameter: N/A
# Example: If num is 16 the output should be 53 as 53 is the 16th prime number

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
		
user_num = int(input("nth number: "))		
		
count = []
x = 1

while len(count) < user_num:
	x += 1
	if prime_pick(x):
		count = count + [x]
print (count[-1])
	
#http://coderbyte.com/CodingArea/Editor.php?ct=Prime%20Mover&lan=Python