import math
import turtle

def main():
#creates screen with attributes
    wn = turtle.Screen()
    wn.setworldcoordinates(0, -1, 1000, 1)
    wn.bgcolor(gray)
    
fred = turtle.Turtle()
screen = turtle.Screen()

#code for Sin Wave
for x in range(700):
    y = math.sin(math.radians(x))
    fred.goto(x,y)

wn.exitonclick()

main()
