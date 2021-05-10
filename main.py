'''
Functions

Python function
- Bundle a set of code that you want to use repeatedly


Define a Function
def FUNCTIONNAME():
	BODY



import turtle
import random

pen = turtle.Turtle()

def drawShapes(radius, side):
  pen.circle(radius, 360, side)

for i in range(10):
  pen.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  drawShapes(100, 3 + i)	
'''
























import turtle
import random

# start out with showing the game
# set up turtle to draw

turtle.speed(100)
turtle.color("red")
turtle.penup()
turtle.goto(-140,140)

# do the track 
# track goes from 0-15 so for loop needs to be 16

for i in range(16):
  
  turtle.pendown()
  turtle.write(i)
  turtle.right(90)
  turtle.penup()
  turtle.forward(10)
  turtle.pendown()
  turtle.forward(150)
  turtle.penup()
  turtle.backward(160)
  turtle.left(90)
  turtle.forward(20)

  # this will be diagonal so ask them why and have them think and then 
  # change turtle.backward(160)

turtle.hideturtle() # turtle does not need to be there anymore

# creating multiple turtles- do 4
# new variables for names 

lalyn = turtle.Turtle()
lalyn.shape("turtle")
lalyn.color("orchid")
lalyn.penup()
lalyn.goto(-160,100)
lalyn.pendown()

celine = turtle.Turtle()
celine.shape("turtle")
celine.color("gold")
celine.penup()
celine.goto(-160,70)
celine.pendown()

richard = turtle.Turtle()
richard.shape("turtle")
richard.color("maroon")
richard.penup()
richard.goto(-160,40)
richard.pendown()

brandon = turtle.Turtle()
brandon.shape("turtle")
brandon.color("blue")
brandon.penup()
brandon.goto(-160,10)
brandon.pendown()

# make sure the turtles are in the right spot
# we want the turtles to move and randomly now so it is a fair retrace
# random is kind of like turtle where we have to import it to use its functionalities
# so at the top we want to import random 

for i in range(105):
  # we want the computer to decide how fast the turtles are going
  lalyn.forward(random.randint(1,5)) # we dont want the turtle to go TOO fast 
  celine.forward(random.randint(1,5))
  richard.forward(random.randint(1,5))
  brandon.forward(random.randint(1,5))