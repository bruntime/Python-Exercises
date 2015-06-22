#Turtle Tutorial

from turtle import *

wn = turtle.screen()
wn.bgcolor('lightblue')
tess = turtle.Turtle()
tess.shape('turtle')
tess.color('blue')

tess.penup()
size = 20
for i in range(30):
	tess.stamp()
	size = size + 3
	tess.forward(size)
	tess.right(24)

wn.mainloop()

#http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html