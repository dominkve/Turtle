from turtle import * #imports the turtle module


def curve():  #defines a function for making a curve

  for i in range (200): #makes the following repeat 200 times
      
      rt(1) #rotates the turtle clockwise by 1 degree
      
      fd(1) #the turtle takes one step forwards
    
      
def leaf(): #defines a function for making a leaf
  
  fillcolor("green") #sets up the filling color
  
  begin_fill() #begins tracking what to fill
  
  lt(140) #rotates counter clockwise for 140 degrees
  
  fd(113) #takes 113 steps forwards
  
  curve() #makes a curve
  
  lt(120) #rotates counter clockwise for 120 degrees
  
  curve() #makes a curve
  
  fd(112) #takes 112 steps forwards
  
  end_fill() #fills the shape it created
  

def draw_leaf_at(x, y, angle): #defines the drawing of a leaf based on the x and y cordinates and also the angle of the leaf
    
    penup() #lifts the pen up
    
    setpos(x, y) #set's the turtle x and y cordinates
    
    setheading(angle) # set's the angle of the leaf
    
    pendown() #starts writing again
    
    leaf() #draws the leaf

# Initial setup

penup() #lifts the pen

setpos(0.00, 20.00) #sets the position to (0, 20)

pendown() # write again

# Draw four leaves rotated by 90 degrees
angles = [0, 90, 180, 270] #sets the angles for all four leafs

positions = [(0, 20), (-20, 0), (0, -20), (20, 0)] #sets the positions of all the leaves


for i in range(4): #makes a loop which will repeat four times

    draw_leaf_at(positions[i][0], positions[i][1], angles[i]) #tells the turtle to draw a leaf at the right cordinates and the right angle according to which of the four it is

ht() #hides the turtle