import turtle
import math

#part A
def drawSquare(t, sz): #sets instructions for drawing square
	for i in range(4): #range goes to number of sides of the polygon
		t.forward(sz) #forward by x size
		t.left(90) #angle calculated by 360/n with n = number of sides

def drawTriangle(t, sz): #sets instructions for drawing triangle
	for i in range(3):
		t.forward(sz)
		t.left(120)

def drawOctagon(t, sz): #sets intstructions for drawing octagon
	for i in range(8):
		t.forward(sz)
		t.left(45)

#part B
def drawPolygon(t, side_length, num_sides): #instructions for any polygon
	for i in range(num_sides):
		t.forward(side_length)
		t.left(360/num_sides)

def drawCircle(t, any_radius):
	circumference = 2 * math.pi * any_radius
	sideLength = circumference / 360 #the radius
	t.penup()
	t.goto(0,0 - any_radius)
	t.pendown()
	drawPolygon(t, sideLength, 360)
	t.penup()
	t.goto(0,0)

def drawFilledCircle(t, any_radius, color): #draws a filled circle with any radius
	t.color(color)
	t.begin_fill()
	drawCircle(t,any_radius)
	t.end_fill()

def main():
	wn = turtle.Screen()

	#names of different turtles used for square, triangle, etc.
	square = turtle.Turtle()
	triangle = turtle.Turtle()
	octagon = turtle.Turtle()
	polygon = turtle.Turtle()
	misc = turtle.Turtle()
	may = turtle.Turtle()
	mark = turtle.Turtle()

	#defines shape and color for each turtle
	may.shape('turtle')
	misc.shape('turtle')
	misc.color('black')
	square.shape('turtle')
	square.color('#d3d3d3')
	triangle.color('#00ced1')
	triangle.shape('turtle')
	octagon.color('#ff69b4')
	octagon.shape('turtle')
	polygon.color('#add8e6')
	polygon.shape('turtle')
	mark.color('pink')
	mark.shape('turtle')

	#executes drawing of different polygons
	drawSquare(square, 120)
	drawTriangle(triangle, 120)
	drawOctagon(octagon, 120)
	drawPolygon(polygon, 85, 10)
	drawCircle(misc, 90)
	drawFilledCircle(may, 50, "purple")


	drawPolygon(mark,1,360) #EXTRA CREDIT


	wn.exitonclick() #click the screen to exit


main()
