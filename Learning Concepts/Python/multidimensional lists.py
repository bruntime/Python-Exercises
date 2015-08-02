#Multidimensional Lists

shows = [
				[["Happy Days", "Comedy", 255],["Frasier", "Comedy", 264]],
				[["Grey's Anatomy", "Drama", 228],["Bones", "Drama", 200]],
				[["Stargate, SG1", "Sci-Fi", 214],["Supernatural", "Sci-Fi", 204]]
			  ]

#prints	entire list of shows	  
print (shows)

#prints set of list on separate line
for x in range(len(shows)):
			print (shows[x])

#prints each list on separate line
for x in range(len(shows)):
	for y in range(len(shows[x])):
			print (shows[x][y])			

#prints each list element on separate line			
for x in range(len(shows)):
	for y in range(len(shows[x])):
		for z in range(len(shows)):
			print (shows[x][y][z])

#search and print list based on a specific element (i.e. print only Sci-Fi shows)?
#function not working			
def find (x, shows):
	for item in shows:
		item == "Sci-Fi"
		if x(item):
			return item