# Take an array of numbers stored in arr and return 1 if the mode equals the mean, 0 if they don't equal each other 
# Example: [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)). 
# The array will not be empty, will only contain positive integers, and will not contain more than one mode.

nums = []

while len(nums) < 10:
	txt = int(raw_input("Enter number : "))
	nums = nums + [txt]
	
mean = sum(nums) / len(nums)

for x in nums:
	mode = nums.count(x)
print nums
print mean
	

