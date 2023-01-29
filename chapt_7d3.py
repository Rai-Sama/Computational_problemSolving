"""
Solution to the development problem #3 from Chapter 7
Creates a geometric animation using turtle graphics and the stack module created in section 7.3.8
"""

from chapt_7_3_8 import * # Note -- name of the file has been changed to chapt_7.3.8 for convenience
import turtle
import time
import random

initial_pos = (-10, -10)
colors = ['red', 'blue', 'green']

stack = createstack()

for i in range(1, 6):
	color = random.choice(colors)
	curr_pos = (initial_pos[0] * i*2, initial_pos[1] * i*2) # bottom left
	length = abs(curr_pos[0]) - curr_pos[0] # length of equilateral turtle_pen
	turtle_pen = turtle.Turtle(visible=False) 
	turtle_pen.penup()

	turtle_pen.setposition(curr_pos[0], curr_pos[1]) # bottom-left corner
	
	turtle_pen.pendown()
	turtle_pen.color(color)

	turtle_pen.setheading(0) # bottom edge direction
	turtle_pen.forward(length) # bottom edge

	turtle_pen.left(120) # right-edge direction (120 degrees because it's equilateral)	
	turtle_pen.forward(length) # right edge

	turtle_pen.left(120) # left-edge direction(120 degrees because it's equilateral)
	turtle_pen.forward(length) # left edge
	stack = push(stack, turtle_pen)

for i in range(5):
	triangle = peek(stack)
	triangle.clear()
	stack = pop(stack)
	time.sleep(1)
