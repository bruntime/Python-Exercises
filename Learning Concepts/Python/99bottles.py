#Exercise: 99 Bottles of Ale

x = 100

while x > 1:
	x -= 1
	print x, "bottles of ale on the wall", x, "bottles of ale"
	print "Take one down and pass it around",  (x - 1) , "bottles of ale on the wall."
	if x == 1:
		print "You just ran out go to the store and buy some more."