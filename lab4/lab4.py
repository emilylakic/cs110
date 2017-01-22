import math
import turtle

#Window Setup
def setUpWindow(s):
	s.setworldcoordinates(-500, -1, 500, 1) #(-500,-1) and (500,1)
	s.bgcolor("gray")

#Turtle Setup
def setUpTurtle(t):
	t.goto(500,0)
	t.goto(0,0)
	t.goto(-500,0)
	t.goto(0,0)
	t.goto(0,1)
	t.goto(0,0)
	t.goto(0,-1)
	t.goto(0,0)

#SIN Wave
def drawSin(t):
	for x in range(361):
		y = math.sin(math.radians(x))
		t.goto(x,y)

#COS Wave
def drawCosineCurve(t):
	t.up()
	t.goto(0,1)
	t.down()
	for x in range(361):
		y = math.cos(math.radians(x))
		t.goto(x,y)

def main():
	wn = turtle.Screen()
	setUpWindow(wn)
	emily = turtle.Turtle()
	emily.shape("turtle")
	emily.color("black")
	setUpTurtle(emily)
	emily.color("blue")
	drawSin(emily)
	emily.color("purple")
	drawCosineCurve(emily)
	wn.exitonclick()

main()
