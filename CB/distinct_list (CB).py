# Take an array of numbers and determine the total number of duplicate entries. 
# For example if the input is [1, 2, 2, 2, 3] then your program should output 2 because there are two duplicates of one of the elements. 

def distinct_list(arr):

list_of_nums = []

count = 0

a = -1
b = 0

#3) compare elements in list and determine total duplicate entries		
while list_of_nums[a] != list_of_nums[-1]:
	a += 1
	b += 1
	if list_of_nums[a] == list_of_nums[b]:
		count += 1
		print a
		print b
		print count

#1) accept numbers from user		
print "Enter numbers. When done entering numbers, type no."
		
user_num = 0
while user_num != "no":		
	user_num = raw_input("Numbers: ")
	list_of_nums = list_of_nums + [user_num]

list_of_nums.pop(-1)	
print list_of_nums

#2) pass list through function
distinct_list(list_of_nums)