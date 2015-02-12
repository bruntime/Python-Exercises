#Project Euler

#Problem #6

# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

import math

i = 0
squares = []

while i < 10:
	i += 1
	square_num = math.pow (i, 2)
	squares.append(square_num)

sum_square_num = sum(squares)
	
print "First 10 numbers squared", squares

# Next step: add first 10 natural numbers then square sum
# Final step: Then subtract total sum of natural numbers by the squares of the natural numbers