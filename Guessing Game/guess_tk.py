#project: Guessing Game using Tkinter

from Tkinter import *
import Tkinter
import tkMessageBox
import random

number = random.randint(0, 100)
guess_total = 0
num_guess = 6

root = Tkinter.Tk()
root.title("Guessing Game")
root.geometry("250x100")

guess = Label (root, text = "Guess")
guess_txtbx = Entry (bd = 4)

def check_guess():	
	
	global guess_total
	global num_guess
	
	txtbx_guess = int(guess_txtbx.get())
	
#Issue:	Unable to escape initial guess, function iterates 6 times (the number of guesses allowed)
#Pop up window does not close upon clicking "OK" button
	
	while guess_total < num_guess:
		guess_total += 1
		if txtbx_guess < 0 or txtbx_guess > 100:
			tkMessageBox.showinfo("User Guess", "Please enter a number within the range of 0 and 100. Please try again.")
		if txtbx_guess < number:
			tkMessageBox.showinfo("User Guess", "Wrong. Higher.")
		if txtbx_guess > number:
			tkMessageBox.showinfo("User Guess", "Wrong. Lower.")
		if txtbx_guess == number:
			tkMessageBox.showinfo("User Guess", "Correct. YAY!!!!")
				
submit_btn = Button(root, text = "Take Guess", height = 6, command = check_guess)

guess.pack()
guess_txtbx.pack()
submit_btn.pack(padx = 4, pady = 4)
root.mainloop()