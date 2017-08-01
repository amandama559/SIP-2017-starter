from turtle import *
import math

t = Turtle()
#using user input to change color of shape
userInput = input("What color do you want your shape to be?")
t.pencolor(userInput)
#userinput is used to ask how many sides user wants
sides = input("How many sides do you want?")
userSides = int(sides)
#user input used to ask user number of shapes
shapes = input("How many shapes do you want?")
userShapes = int(shapes)

#beginning position
setup(500,500)
x_pos = 0
y_pos = 0

#to not show the change of coordinates
t.penup()
t.setposition(x_pos, y_pos)
t.pendown()
#loop to repeat how many times shape is drawn
for numshapes in range (0,userShapes):
    t.penup()
    t.right(360/userSides)
#loop to draw shape
    for steps in range(0,userSides):
        t.pendown()
        t.forward(100)#moves 100 steps
        t.right(360/userSides)#shows how many sides divide 360 by #of sides inputted(angle)


done()

t.forward(200)#move after drawing so each drawn doesn't overlap
