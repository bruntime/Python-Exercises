#Project: Fibonacci Sequence

list_of_nums = [0, 1]

a = -1
b = 0

while list_of_nums[-1] <4000000:

	a += 1
	b += 1
	
	sum = list_of_nums[a] + list_of_nums[b]
	list_of_nums.append(sum)
	
print list_of_nums

for x in list_of_nums:
	if x % 2 == 0:
		print x




