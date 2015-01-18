from Tkinter import *

#creates window
root = Tk()

#window title
root.title("Feedback Form")

#window size
root.geometry("250x250")

#menu for exiting
menubar = Menu(root)
filemenu = Menu (menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Exit", command = root.quit)

#form label
labelframe = LabelFrame(root, text = "Favourite Movies Feedback Form", bg = "white")
labelframe.pack(fill="both", expand="yes")

#textboxes for form
name = Label(labelframe, text = "First Name", bg = "yellow")
name_txbx = Entry(labelframe, bd = 2)

show = Label(labelframe, text = "Favourite Television Show", bg = "yellow")
show_txbx = Entry (labelframe, bd = 2)

seasons = Label(labelframe, text="# of Seasons", bg = "yellow")
seasons_txbx = Entry(labelframe, bd = 2)

name.pack(padx = 10, pady = 10), name_txbx.pack()
show.pack(padx = 10, pady = 10), show_txbx.pack()
seasons.pack(padx = 10, pady = 10), seasons_txbx.pack()

root.config(menu = menubar)
root.mainloop()