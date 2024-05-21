from turtle import *  # import the turtle module

# set up
n = 200  # creates a variable n and sets it to 200

setpos(n/2, 0)  # sets the position to (n/2, 0) which in this case is (100, 0)

tolerance = 1e-5  # creates a variable for equating the float stuff

# drawing
while True:  # makes a loop

  rt(170)  # rotates the turtle for 170 degrees clockwise

  fd(200)  # the turtle goes forward 200 steps

  x, y = pos()  # equates variables x and y to the pos of the turtle, which is (x, y)
  if abs(x - n/2) < tolerance and abs(y) < tolerance:  # checks the turtles position to see if its returned to the starting point

    break  # exits the loop

# finishing touches
ht()  # hides the turtle
