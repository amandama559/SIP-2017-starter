from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0

t.penup()
t.setposition(x_pos, y_pos)

print(t.position())

t.pendown()
y_pos = 50
t.setposition(x_pos, y_pos)

print(t.position())

x_pos = 50
t.setposition(x_pos, y_pos)

print(t.position())

y_pos = 0
t.setposition(x_pos, y_pos)

print(t.position())

x_pos = 0
t.setposition(x_pos, y_pos)

print(t.position())



exitonclick()












# Close window on click.
