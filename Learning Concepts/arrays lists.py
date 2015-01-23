#Arrays and Lists

print range (3, 20)

quote = "Either I will find a way, or I will make one. Philip Sidney"

print quote[46], quote[51], quote [53]

print (quote[0:7], quote[9:14])

first_10_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print first_10_letters[6]

numbers = [45, 8, 20, 13, 9, 1, 155, 80]

print numbers [3]

for x in numbers:
	if x % 10 == 0:
		print "numbers in array divisible by 10 are", x

for x in range (2, 16):
	if x % 3 == 0:
		print x
