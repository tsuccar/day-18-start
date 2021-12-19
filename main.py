import turtle
from turtle import Turtle, Screen
import random

##########################
# Exercise 1 Draw Polygons
##########################
# class Form:
# 	def __init__(self,name,sides,angle,color):
# 		self.name=name
# 		self.sides=sides
# 		self.angle=angle
# 		self.color=color
#
# class FormList:
# 	def __init__(self):
# 		self.menu = [Form(name = "Triangle", sides = 3, angle = 60, color = "red"),
# 					Form(name = "Square", sides = 4, angle = 90, color = "blue"),
# 					Form(name = "Hexagon", sides = 5, angle = 108, color = "black"),
# 					Form(name = "Pentagon", sides = 6, angle = 120, color = "yellow")
# 					]
#
# def draw_turtle (objt):
# 	sides=objt.sides
# 	angle=objt.angle
# 	color=objt.color
# 	for _ in range(sides):
# 		tim.pencolor(color)
# 		tim.forward(100)
# 		tim.right(180 - angle)
#
# tim = Turtle()
# tim.shape('turtle')
# tim.color('red')
# formlist = FormList()
# my_object_form_list = formlist.menu
#
# for each in my_object_form_list:
# 	draw_turtle(each)

# ###############################
# # Exercise #2 - Draw Random Walk
# ################################
# def walk (color,angle):
# 	tim.pensize(10)
# 	tim.seth(angle)
# 	tim.speed(3)
# 	tim.color(color)
# 	tim.forward(20)
#
# def randomize():
# 	color_selection=random.choice(["CornflowerBlue","DarkOrchid","DeepSkyBlue","LightSeaGreen",
# 	                               "wheat","SlateGray","SeaGreen"])
# 	angle_choice=random.choice([0,90,180,270])
# 	print(color_selection,angle_choice)
# 	print(type(angle_choice))
# 	return color_selection,angle_choice
#
# tim = Turtle()
# tim.shape('turtle')
#
# while True:
# 	color,angle=randomize()
# 	walk(color,angle)
###############################
# Exercise #3 - Draw Random Walk - with RGB(random color instead of a list)
################################
# turtle.colormode(255)
#
# def walk(color, angle):
# 	tim.pensize(10)
# 	tim.seth(angle)
# 	tim.speed(3)
# 	tim.color(color)
# 	tim.forward(20)
#
#
# def random_color():
# 	r=random.randint(0,255)
# 	g=random.randint(0,255)
# 	b=random.randint(0,255)
# 	return(r,g,b)
#
# def random_direction():
# 	angle_choice = random.choice([0, 90, 180, 270])
# 	return angle_choice
#
#
# tim = Turtle()
# tim.shape('turtle')
#
# while True:
# 	color=random_color()
# 	angle=random_direction()
# 	walk(color, angle)
###############################
# Exercise #4 - Draw Random Walk - with RGB(random color instead of a list)
################################
turtle.colormode(255)
#
def random_color():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	return(r,g,b)

def draw_circle(angle):
    tim.seth(angle)
    tim.speed("fastest")
    tim.color(random_color())
    tim.circle(100, 360)
    
tim = Turtle()
tim.shape('turtle')

for angle in range(360):
        draw_circle(angle)
