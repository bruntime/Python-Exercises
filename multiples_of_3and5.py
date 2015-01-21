#Multiples of 3 and/or 5 under 1000

print ("\nSmall Exercise on multiples of 3 and 5\n")

for x in range (1, 1000):
	if x % 3 == 0:
		print ("This is a multiple of 3:"), x
	if x % 5 == 0:
		print ("This is a multiple of 5:"), x
	if x % 3 == 0 and x % 5 == 0:
		print ("This is a multiple of 3 and 5:"), x