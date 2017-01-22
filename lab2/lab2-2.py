import turtle
import random
screen = turtle.Screen()
screen.bgcolor('lightblue')

andrew = turtle.Turtle()
hayley = turtle.Turtle()
andrew.color('green')
hayley.color('purple')
andrew.shape('turtle')
hayley.shape('turtle')

andrew.up()
hayley.up()

andrew.goto(-100,20)
hayley.goto(-100,20)

for direction in range(0, 360, 90):
	andrew.forward(84)
	hayley.forward(90)

screen.exitonclick()

import os
import turtle

def main():
    monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
    for month in monthList:
        print ("One of the months of the year is ", month)

    numList = [12, 10, 32, 3, 99]
    for num in numList:
        print (num,num**2)

    wn = turtle.Screen()
    terp = turtle.Turtle()
    terp.shape('turtle')
    terp.color('blue','purple')
    for i in range(3):
        terp.left(120)
        terp.forward(20)

    t = turtle.Turtle()
    t.shape('turtle')
    t.color('green')
    for i in range(4):
        t.fd(50)
        t.left(90)

    tur = turtle.Turtle()
    tur.shape('turtle')
    tur.color('black')
    for i in range(6):
        tur.left(60)
        tur.forward(60)

    tp = turtle.Turtle()
    tp.shape('turtle')
    tp.color('magenta')
    for i in range(8):
        tp.fd(45)
        tp.left(45)

    side = int(input('How many sides? '))
    length = int(input('How long is a side? '))
    color = input('What is the outline color? ')
    fill = input('What is the fill color? ')

    tin = turtle.Turtle()
    tin.shape('turtle')
    tin.color(color)
    tin.fillcolor(fill)
    degree = 360/side
    for i in range(side):
        tin.fd(length)
        tin.left(degree)

    os.system("man")
    os.system("pwd")
    os.system("mkdir")
    os.system("rm")
    os.system("cd")
    os.system("ls")
    os.system("mv")
    os.system("cp")
    os.system("python3")

    wn.exitonclick()
main()
