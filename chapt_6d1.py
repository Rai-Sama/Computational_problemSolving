"""
Random walk implementation -- useful for simulating random molecule movements, etc.
Here, I have not implemented the turning back option
because I got tired of writing all the if conditions. It's easy enough to add
"""
import turtle
import random
import time


def citylayout():
	"""
	Drawing the grid layout to act as the city 
	"""
	blocks = 8 
	starting_pt = (-200, -200)
	grid_lines = []
	for block in range(blocks+1):
		grid_line = turtle.Turtle(visible=False)
		grid_line.speed(0)
		grid_line.penup()
		grid_line.setposition(starting_pt[0] + 50 * block, starting_pt[1])
		grid_line.pendown()
		grid_line.setposition(starting_pt[0] + 50 * block, 200)
		

		grid_line2 = turtle.Turtle(visible=False)
		grid_line2.speed(0)
		grid_line2.penup()
		grid_line2.setposition(starting_pt[0], starting_pt[1] + 50 * block)
		grid_line2.pendown()
		grid_line2.setposition(200, starting_pt[1] + 50 * block)


def housesetup():
	"""
	Drawing the house in its position
	"""
	house = turtle.Turtle(visible=False)
	house.speed(0)
	house.penup()
	house.setposition(25, 175)
	house.shape('triangle')
	#house.fillcolor('blue')
	house.setheading(90)
	house.showturtle()
	return house


def drunk_walking(man, house):
	"""
	Simulation of drunk walking given the man and the house.
	"""
	man.setheading(90)
	man.pendown() # just to see nice patterns while it walks randomly
	athome = False
	message = turtle.Turtle(visible=False)
	message.penup()
	message.setposition(-200, -250)
	message.pendown()

	

	while not athome:
		no_lims = True
		forw_lim = 50
		left_lim = 50
		right_lim = 50
		if man.xcor() - 50 <= -200: # Left-most blocks
			if man.heading() == 90: # heading up
				left_lim = 0
				right_lim = 50
				if man.ycor() + 50 >= 200: # top-left corner
					forw_lim = 0
				else:
					forw_lim = 50
				no_lims = False
			elif man.heading() == 270: # heading down
				right_lim = 0
				left_lim =  50
				if man.ycor() - 50 <= -200: # bottom-left corner
					forw_lim = 0
				else:
					forw_lim = 50
				no_lims = False
			elif man.heading() == 180: # heading left
				forw_lim = 0
				left_lim = 50
				right_lim = 50
				no_lims = False
			# Add heading right conditions if you want to add turning back as an option
		
		elif man.xcor() + 50 >= 200: # right-most blocks
			if man.heading() == 90: # heading up
				right_lim = 0
				left_lim = 50
				if man.ycor() +  50 >= 200: # top-right corner
					forw_lim = 0
				else:
					forw_lim = 50
				no_lims = False
			elif man.heading() == 270: # heading down
				left_lim = 0
				right_lim =  50
				if man.ycor() - 50 <= -200: # bottom-right corner
					forw_lim = 0
				else:
					forw_lim = 50
				no_lims = False
			elif man.heading() == 0: # heading right
				forw_lim = 0
				left_lim = 50
				right_lim = 50
				no_lims = False
			# Add heading left conditions if you want to add turning back as an option

		if man.ycor() -  50 <= -200: # bottom-most blocks
			if man.heading() == 180: # heading left
				left_lim = 0
				right_lim = 50
				if man.xcor() - 50 <= -200: # bottom-left corner
					forw_lim = 0
				else:
					forw_lim = 50
				no_lims = False
			elif man.heading() == 0: # heading right
				right_lim = 0
				left_lim =  50
				if man.xcor() + 50 >= 200:# bottom right corner
					forw_lim = 0
				else:
					forw_lim = 50
				no_lims = False
			elif man.heading() == 270: # heading down
				forw_lim = 0
				left_lim = 50
				right_lim = 50
				no_lims = False
			# Add heading up conditions if you want to add turning back as an option

		elif man.ycor() + 50 >= 200: # top-most blocks
			if man.heading() == 180: # heading left
				right_lim = 0
				left_lim = 50
				if man.xcor() - 50 <= -200: # top-left blocks again -- not required
					forw_lim = 0
				else:
					forw_lim = 50
				no_lims = False
			elif man.heading() == 0: # heading right
				left_lim = 0
				right_lim = 50
				if man.xcor() + 50 >= 200: # top-right corner again --not required
					forw_lim = 0
				else:
					forw_lim = 50
				no_lims = False
			elif man.heading() == 90: # heading up
				forw_lim = 0
				left_lim = 50
				right_lim = 50
				no_lims = False
			# Add heading down conditions if you want to add turning back as an option
			

		if no_lims:
			print("No limitss")
			temp = random.randint(0, 2)
			if temp == 2:
				man.right(90)
			elif temp == 1:
				man.left(90)
			else:
				pass
		else:
			if left_lim == 50 and forw_lim == 50:
				print("not righttttttt")
				temp = random.randint(0, 1)
				if temp == 1:
					man.left(90)
				else:
					pass
			elif right_lim == 50 and forw_lim == 50:
				print("not leftttttttt")
				temp = random.randint(0, 1)
				if temp:
					man.right(90)
				else:
					pass
			elif right_lim == 50 and left_lim == 50:
				print("not forwarddddddddd")
				temp = random.randint(0, 1)
				if temp:
					man.left(90)
				else:
					man.right(90)
			elif right_lim == 50:
				man.right(90)
			elif left_lim == 50:
				man.left(90)


		man.forward(50)
		print(int(round(man.xcor())), int(round(man.ycor())), man.heading())
		if(round(man.xcor()) == 25 and round(man.ycor()) == 175 ):
			man.hideturtle()
			house.fillcolor('green')
			message.color("red")
			message.write("The drunkard is now home", font=("Verdana", 20, "normal"))
			
			athome = True


turtle.setup(800, 600)
window = turtle.Screen()
window.title("Random walk")

citylayout() # drawing the city
house = housesetup() # adding the house

man = turtle.Turtle(visible=False)
man.penup()
man.speed(0)
man.setposition(-175, -175)
man.showturtle()
man.speed(6)
turtle.register_shape('files_etc/horse_img.gif') # adding shape for drunkard
man.shape('files_etc/horse_img.gif')

drunk_walking(man, house)

time.sleep(5) # 5 seconds to see that the drunkard has reached home