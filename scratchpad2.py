#Displays a circle bouncing around the canvas window.
from tkinter import *
window = Tk()
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()
x0 = 0		# initial left-most edge of ball
y0 = 0		# initial top-most edge of ball
x1 = x0+20		# inital right-most edge of ball
y1 = y0+20	# you've probably got the idea by now.
dx = 2
dy = 3
tail = x0,y0,x0-50,y0-50
# create ball:
which = canvas.create_oval(x0,y0,x1,y1,fill="blue", tag='blueBall')
canvas.create_line(tail,fill="red",tag='myline')
while True:
    canvas.move('blueBall', dx, dy)
    canvas.move('myline',dx,dy)
    canvas.after(0)
    canvas.update()
    # the next 4 if statements check if the ball hits a wall: if it hits
    # a floor/ceiling its y-velocity reverses and it if hits a left/right
    # wall its x-velocity reverses
    if x1 >= 400:
        dx = -2
    if y1  >= 300:
        dy = -3
    if y0 < 0:
        dy = 3
    if x0 < 0:
        dx = 2
    x0 += dx
    x1 += dx
    y0 += dy
    y1 += dy
window.mainloop()