extinct_creatures = open("extinct.txt", "r")

print extinct_creatures.read(10) #reads based on size
print extinct_creatures.readline(20) #reads single line

for i, line in extinct_creatures:
	if i == 4:
		print "Line 4", i
	if i == 10:
		print "Line 10", i #ValueError: too many values to unpack 

