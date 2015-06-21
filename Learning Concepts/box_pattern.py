from turtle import *

speed('faster')

bgcolor('blue')
screensize(40, 40)

color('red', 'orange')
pensize(6)
begin_fill()

while True:

	circle(100)
	forward(5)
	down()
	left(20)
	
	if abs(pos()) < 1:
		break
end_fill()
done()