#Return the sum of all the multiples of 3 and 5 that are below a number given by a user. 
#For example: if num is 10, the multiples of 3 and 5 that are below 10 are 3, 5, 6, and 9.
#Adding them up you get 23, so your program should return 23. 
#The integer being passed will be between 1 and 100.

def multipes_3_and_5(num):

	multiples = []

	if num <= 100:
		for x in range(0, num)
			if x % 3 == 0 or x % 5 == 0:
				print x
			
	#place numbers in list
	#add numbers in list
	#print total
	
	if num > 100:
		print "You have entered a number greater than 100." 
		#optional: ask user to try again

user_num = int(raw_input("Enter number between 1 and 100: "))

multipes_3_and_5(user_num)