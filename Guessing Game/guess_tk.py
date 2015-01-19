#project: Guessing Game using Tkinter

from Tkinter import *
import Tkinter
import tkMessageBox
import random

number = 5

root = Tkinter.Tk()
root.title("Guessing Game")
root.geometry("250x100")

guess = Label (root, text = "Guess")
guess_txtbx = Entry (bd = 4)

# def check_guess():
	# txtbx_guess = guess_txtbx.get()
# function to check user guess against number

def submit():
# function to tell user whether their guess is right or wrong	
	tkMessageBox.showinfo("User Guess", "Your guess was right or wrong.")	
	
submit_btn = Button(root, text = "Submit", height = 40, command = submit)

guess.pack()
guess_txtbx.pack()
submit_btn.pack(padx = 5, pady = 5)
root.mainloop()