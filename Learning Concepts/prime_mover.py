# Return the nth prime number
# Example: if num is 16 the output should be 53 as 53 is the 16th prime number

def prime_pick(num):

	nums = []
	
	a = 0
	while a <= num:
		a += 1
		if num % a == 0:
		 nums.append(a)
	if len(nums) > 2:
		return False
	else:
		return True

prime_nums = []
	
user_num = int(raw_input("Your number: "))
prime_num_select = int(raw_input("Prime Number Selection: "))

for x in xrange(2, user_num+1):
	if prime_pick(x):
		prime_nums = prime_nums + [x]

print prime_nums
print prime_nums[prime_num_select-1]