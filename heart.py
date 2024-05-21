from turtle import * #imports the turtle module


def curve():  #defines a function for making a curve

  for i in range (200): #makes the following repeat 200 times
      
      rt(1) #rotates the turtle clockwise by 1 degree
      
      fd(1) #the turtle takes one step forwards
      
def heart(): #defines a function for making a heart
  
  fillcolor("red") #sets up the filling color
  
  begin_fill() #begins tracking what to fill
  
  lt(140) #rotates counter clockwise for 140 degrees
  
  fd(113) #takes 113 steps forwards
  
  curve() #makes a curve
  
  lt(120) #rotates counter clockwise for 120 degrees
  
  curve() #makes a curve
  
  fd(112) #takes 112 steps forwards
  
  end_fill() #fills the shape it created
  
heart() #makes a heart

ht() #hides the turtle