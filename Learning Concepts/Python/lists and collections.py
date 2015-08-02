#Multidimensional List - cleaner version

comedy = ["Happy Days", 255],["Frasier", 264]
drama = ["Grey's Anatomy", 228],["Bones", 200]
scifi = ["Stargate, SG1", 214],["Supernatural", 204]

shows = [comedy, drama, scifi]

question = raw_input("What's your favourite genre? ")

if question == "comedy":
	print "These are the comedies available to watch and the number of episodes", shows[0]
elif question == "drama":
	print "These are the drama available to watch and the number of episodes", shows [1]
elif question == "sci-fi" or question == "scifi":
	print "These are the sci-fi available to watch and the number of episodes", shows [2]
else:
	print "There are no shows available for your favourite genre."

#Collection

fish = {"bass" : 1, "pike" : 2, "alligatorfish" : 3,  "catfish" : 4}

fish_type = raw_input("What kind of fish do you want? ")

if fish_type == "bass" or fish_type == "pike" or fish_type =="alligatorfish" or fish_type =="catfish":
	print ("This fish is in the collection")
else:
	print ("This fish is not in the collection")
	