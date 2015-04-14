def intro():
	
	town_name = 'Blahville'
	current_time = 'this time'
	current_date = 'today'
	
	print '''
	Ah! Came to play, huh?
	Right now in %s, its %s on %s.
	How about we get started?
	''' %(town_name, current_time, current_date)
	
	print "\nNow, hang on... You are ...?"
	
def name_choice(name):

	print 'Oh,', name, 'is it?'
	print 'Nice name! I like it!'