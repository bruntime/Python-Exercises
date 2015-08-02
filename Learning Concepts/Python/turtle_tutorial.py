#Turtle Graphics Tutorial

from turtle import *

#Create 2 pen objects
pen1 = Pen() #constructor, constructing object
pen2 = Pen()

#Set the screen's background color
pen1.screen.bgcolor('red')

#Set the pen colors
pen1.color('blue')
pen2.color('green')

#Move pens
pen1.forward(100)
pen2.backward(100)

#Move the pen without leaving a trail
pen1.up() #life up the pen
pen1.goto(-100, 100)
pen1.down() #set the pen back down

#Draw a circle
pen1.circle(50)

#Draw a half-circle
pen2.circle(50, -180)

#move the pen
pen1.up() #don't forget to lift the pen up
pen1.goto(100, 200)
pen1.down()

#Fill a shape (triangle)
pen1.begin_fill()
for i in range(3):
	pen1.forward(75)
	pen1.right(360/3)
pen1.end_fill()

#17-sided polygon
pen2.begin_fill()
for i in range(11):
	pen2.bk(100)
	pen2.left(360.0/11)
pen2.end_fill()

#https://www.youtube.com/watch?v=6lyHpNjXqMI