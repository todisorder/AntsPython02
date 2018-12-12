#import matplotlib.pyplot as plt
#import numpy as np
#from random import *
#from tkinter import *
#from tkinter import messagebox

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

wn.register_shape("triangle", ((5,-3), (0,5), (-5,-3), (1,7)))

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("hotpink")
tess.pensize(1)
tess.shape("triangle")

alex = turtle.Turtle()           # create alex

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()

