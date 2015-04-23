import time
import Tkinter
import tkMessageBox

def intro():
	
	town_name = 'Blahville'
	current_time = time.strftime("%H:%M:%S", time.localtime(666))
	current_date = 'today'
	
	print '''
	[Rover:]
	
	All righty! Sorry to keep
	you waiting. I heard you
	were moving in, so I came
	to get you! Nice, huh?
	
	Aaaah, life on your own...
	I know that's exactly what
	you're thinking right now.
	
	Nobody to tell you what to
	do! Free to live exactly as
	you please! Sign me UP!
	
	Oh yeah, a new house,
	a new neighborhood, some
	new friends...
	
	A fresh, new start and a
	whole world of possible
	encounters await. I mean...
	How sweet is that?!
	
	Ah! Came to play, huh?
	Right now in %s, its %s.
	How about we get started?
	''' %(town_name, current_time)
	
	return '\nNow, hang on... You are ...?'
	
def name_choice(name):

	print 'Oh,', name, 'is it?'
	print 'Nice name! I like it!'
	
	top = Tkinter.Tk()
	
	#Popup window for user selection
	
	# message = 
	
	# print '''
	# 1- Cool, eh?
	# 2- Cute, hm?
	# 3- That's not it
	# '''
	
	# tkMessageBox.showinfo(message)
	
	user_selection  = raw_input('Please make a selection (1, 2, or 3)')
	
	# top.mainloop()
	
	if  user_selection == '1':
		player_gender = raw_input('So you are a boy? (Y or N)')
		if player_gender == 'Y':
			print ''' 
			Yeah, yeah, completely. 
			It's fun and masculine. 
			The perfect name for you
			'''
			
		elif player_gender == 'N':
			return name, 'not a boy'
	elif user_selection == '2':
		print 'You are a girl?'
	elif user_selection == '3':
		print '''
		What? Did I get it wrong? 
		I need new ears, seriously. 
		Look, I'm sorry about that. Mind telling me again?
		'''
	else:
		return 'That is not a choice'
	
	