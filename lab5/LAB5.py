'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Input from keyboard:
  numberDarts (int)
Tasks allocated to functions:
  setUpDartboard() - invokes setworldcoordinates(), drawSquare(), and
                     drawLine()
  drawSquare() - to outline dartboard
  drawLine() - to draw axes
  drawCircle() - to draw the circle
  inCircle() - determine if dot is in circle
  montePi() - simulation algorithm
'''

# List imports here:
import turtle
import math
import random

# List constants here (NO MAGIC NUMBERS!):
BATCH_OF_DARTS = 5000
BOARD_WIDTH = 2
DOT_SIZE = 2
RIGHT_ANGLE = 90
PEN_SIZE = 3

# This function doesn't return a value
# Draws square given turtle, width and top left XY position
# Use the parameter names given
# param grapher (Turtle)
# param width (int)
# param topLeftX (int)
# param topLeftY (int)
def drawSquare(grapher, width, topLeftX, topLeftY):
    # Don't forget to put pen up and down as appropriate
    grapher.up()
    grapher.goto(topLeftX,topLeftY)
    grapher.down()
    for i in range(4):
        grapher.forward(width)
        grapher.right(90)

# This function doesn't return a value
# Draws axis-lines given turtle and endpoints
# Use the parameter names given
# param grapher (Turtle)
# param xStart (int)
# param yStart (int)
# param xEnd (int)
# param yEnd (int)
def drawLine(grapher, xStart, yStart, xEnd, yEnd):
    # Don't forget to put pen up and down as appropriate
    grapher.up()
    grapher.setpos(xStart,yStart)
    grapher.down()
    grapher.goto(xEnd,yEnd)

# This function doesn't return a value
# Draws circle around the origin with given radius
# Use the parameter names given
# param grapher (Turtle)
# param radius the radius of the circle
def drawCircle(grapher,radius):
    # Look at the turtle library for a function that can make this easier
    for i in range(360):
        grapher.forward((2 * math.pi * radius)/360)
        grapher.left(1)

# This function doesn't return a value
# Sets up 2X2 area with x- and y-axis to simulate dartboard
# Use the parameter names given
# param board - window that will simulate board
# param grapher - turtle that will do drawing
def setUpDartboard(board,grapher):
    # Hint:  you will be using BOARD_WIDTH here!
    # Remember that the order, number, and type of arguments sent to an
    #   invoked function must match the order, number, and type of that
    #   function's parameters
    # However, matching the names of the arguments to the names of the
    #   parameters is not only irrelevant, but in many cases will be impossible
    #   (say when the argument is a named constant or when an argument doesn't
    #   have a name, like when it's 0, 1 or -1)

    # set up 2X2 area and set pensize
    board.setworldcoordinates(-1,-1,1,1) # make at least a 2X2 area
    grapher.pensize(PEN_SIZE)

    # Draw board
    drawSquare(grapher,BOARD_WIDTH,-1,1)

    # Draw x- and y-axes
    drawLine(grapher,0,-1,0,1)
    drawLine(grapher,1,0,-1,0)
    #draw the circle area
    grapher.up()
    grapher.goto(0,-1)
    grapher.down()
    drawCircle(grapher,BOARD_WIDTH/2)

# This function returns a value
# (Predicate Function)
# Determines whether or not dart falls inside unit circle with center at 0,0
# Use the parameter name given
# param dart (Turtle)
# return True if in circle, False if not
def inCircle(dart):
# Look up distance() method on a turtle object
# You'll want to determine if the distance of the dart from the center is
#   in the circle (i.e., <= the circle's radius of 1)
    if dart.distance(0,0) <= 1:
        return True
    else:
        return False

# This function returns a value
# randomly place a 'dart' on the board
# Use the parameter names given
# param dart (Turtle)
def throwDart(dart):
    # Get random x and y coordinates and then position the dart
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    dart.up()
    dart.goto(x,y)
    dart.down()

    # Draw red dot if in circle, blue dot if not
    if inCircle(dart):
        # Increment inCircleCount
        dart.color('red')
        # Draw dot
        dart.dot()
        #return the boolean true
        return True
    else:
        #Set dot color to blue
        dart.color('blue')
        # Draw dot
        dart.dot()
        #return the boolean false
        return False

# This function returns a value
# Algorithm for Monte Carlo simulation
# Use the parameter names given
# param numberDarts (int)
# param dart (Turtle)
# return approximation of pi (float)
def montePi(numberDarts,dart):
#An accumulator is a number that increases by one for every instance of something you are looking for
    # Initialize your accumulator
    inCircleCount = 0
    darts = numberDarts
    while(numberDarts > 0):
        if(throwDart(dart)):
            inCircleCount += 1
        numberDarts -= 1
    approximation_of_pi = (inCircleCount/darts)*4
    # ratio of inCircleCount to numberDarts is pi/4, therefore
    #   ratio * 4 will be approximation += 1 of pi
    # return approximation of pi after 'throwing' all the darts
    return approximation_of_pi


# This is a non-fruitful or void function
#Performs Monte Carlo simulation to generate approximation of Pi
def main():
    # Get number of darts for simulation from user
    numberDarts = int(input("Pick a number of darts: "))
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    window.bgcolor('pink')
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(numberDarts):
        randx = random.uniform(-1,1) #pick random value N b/w -1 and 1
        randy = random.uniform(-1,1) #pick random value N b/w -1 and 1
        darty.up()
        darty.goto(randx,randy)
        darty.down()
        darty.dot('gray') #makes turtle circle and colors it green

    print("\tPart A Complete...")
    print("=========== Part B ===========")
    # Include the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    # Note use of format strings and format specifiers!!
    # We will talk about these on Monday
    numberDarts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))

    print("\nThe estimation of pi using %d virtual darts is %.9f" %(numberDarts, montePi(numberDarts, darty)))
    print("\tPart B Complete...")
    # Keep the window up until dismissed (Hopefully this will work!)
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
