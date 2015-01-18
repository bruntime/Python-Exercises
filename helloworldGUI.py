from Tkinter import *

#creates window
root = Tk()

#window title
root.title("Hello")

#window size
root.geometry("200x50")

name = Label(text = "Hello World", bg = "yellow")

name.pack() #required to show label
root.mainloop()