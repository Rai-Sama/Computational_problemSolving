# Simulating a horse race with turtle graphics

import turtle
import random
import time
from PIL import Image

def generate_horses(num_horses): # Generates 1 turtle for each horse in the race
	horses = []
	for i in range(num_horses):
		horse = turtle.Turtle(visible=False)
		horse.speed(0)
		#horse.hideturtle()
		horse.shape('files_etc/horse_img.gif')
		horses.append(horse)
	return horses


num_horses = 10 # num of horses in the race

interval = 3 # Every 3 seconds one of the horses will move 

img = Image.open("files_etc/horse_img.png")
img.save("files_etc/horse_img.gif")

turtle.setup(800, 600) # setting up the window

window = turtle.Screen()
window.title('Horse Race Simulation')
turtle.register_shape('files_etc/horse_img.gif')

finish_line = []
for i in range(-225, 300, 50):
	line1 = turtle.Turtle(visible=False)
	line1.penup()
	line1.speed(0)
	line1.shape('arrow')
	line1.setposition(-500, i)
	line1.setheading(90)
	line1.showturtle()

	line2 = turtle.Turtle(visible=False)
	line2.penup()
	line2.speed(0)
	line2.setposition(-500, i)
	line2.pendown()
	line2.setposition(200, i)

starting_pt = (200, -200) # Initial position of the bottom most horse on the screen

horses = generate_horses(num_horses)


for horse_num in range(num_horses):
	horses[horse_num].penup()
	horses[horse_num].setposition(starting_pt[0], starting_pt[1] + 50 * horse_num)
	horses[horse_num].setheading(180)
	horses[horse_num].showturtle()
	horses[horse_num].speed(6)

racing = True
window.bgcolor('red')
time.sleep(1)
window.bgcolor('orange')
time.sleep(1)
window.bgcolor('green')
time.sleep(0.5)

while racing:
	r = random.randint(0, num_horses-1)
	horses[r].forward(150)
	if horses[r].position()[0] <= -500:
		racing = False
		print(f"Horse #{r+1} has won the race!")
	#time.sleep(3)





