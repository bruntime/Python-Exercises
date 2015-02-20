# Return the nth prime number
# Example: if num is 16 the output should be 53 as 53 is the 16th prime number

def prime_pick(num):

	a = 0
	nums = []
	
	while a <= num:
		a += 1
		if num % a == 0:
			nums.append(a)
	
	if nums[0] == 1 and nums[1] == num:
		print nums		

prime_nums = []
	
user_num = int(raw_input("Your number: "))
prime_num_select = int(raw_input("Prime Number Selection: "))

for x in xrange(2, user_num+1):
	if prime_pick(user_num):
		prime_nums.append(x)

for x in prime_nums:
	if x == prime_num_select:
		print x