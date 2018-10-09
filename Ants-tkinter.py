#import matplotlib.pyplot as plt
import numpy as np
from random import *
from tkinter import *
from tkinter import messagebox
import turtle
from file_to_be_read_by_python import *



CurrentTime = delta_t


class Ant:
    def __init__(self,posx,posy,velx,vely):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely
        self.posxold = posx
        self.posyold = posy
        self.velxold = velx
        self.velyold = vely
        self.turning_angle = 0.
        self.forcex = 0.
        self.forcey = 0.

    def left_antennax(self):
        return self.posx + SENSING_AREA_RADIUS*np.cos(Angle(self.velx,self.vely) + SensingAreaHalfAngle)
    def left_antennay(self):
        return self.posy + SENSING_AREA_RADIUS*np.sin(Angle(self.velx,self.vely) + SensingAreaHalfAngle)
    def right_antennax(self):
        return self.posx + SENSING_AREA_RADIUS*np.cos(Angle(self.velx,self.vely) - SensingAreaHalfAngle)
    def right_antennay(self):
        return self.posy + SENSING_AREA_RADIUS*np.sin(Angle(self.velx,self.vely) - SensingAreaHalfAngle)

class Droplet:
    def __init__(self,ant,time):
        self.origin_time = time
        self.posx = ant.posx
        self.posy = ant.posy
    def elapsed_time(self):
        return CurrentTime - self.origin_time
    def show(self):
        print(self.posx,self.posy,self.elapsed_time())



AllTheAnts = [0] * NumberOfAnts
AllThePheromone = []

def Angle(x,y):
    return np.arctan2(y,x)

def AngleBetween(x1,y1,x2,y2):
    dot = x1*x2 + y1*y2
    det = x1*y2 - y1*x2
    return  np.arctan2(det,dot)


seed(2632323)

for i in range(NumberOfAnts):
    posx = random()*(x_2-x_1) + x_1
    posy = random()*(y_2-y_1) + y_1
    velx = np.cos(random()*2.*Pi)*NaturalVelocity
    vely = np.sin(random()*2.*Pi)*NaturalVelocity
    AllTheAnts[i] = Ant(posx,posy,velx,vely)                # Create the ants



def Heat(x,y,t):
    aux = (1. / (4.*Pi* Diffusion * t))
    aux *= np.exp(-(x*x + y*y) / (4.*Diffusion*t))
    aux *= np.exp(-Evaporation*t)
    aux *= DropletAmount
    return aux

def FeltPheromone_left(ant):
    result = []
    for ph in AllThePheromone:
        x = ph.posx - ant.left_antennax()
        y = ph.posy - ant.left_antennay()
        t = CurrentTime - ph.origin_time
        result = result+[Heat(x,y,t)]
    return max(Threshold,sum(result))

def FeltPheromone_right(ant):
    result = []
    for ph in AllThePheromone:
        x = ph.posx - ant.right_antennax()
        y = ph.posy - ant.right_antennay()
        t = CurrentTime - ph.origin_time
        result = result+[Heat(x,y,t)]
#        print('res ',result)
    return max(Threshold,sum(result))



def ComputeForcex(ant):
#    print('rrrrrrrrr',  FeltPheromone_right(ant))
#    print('lllllllll',  FeltPheromone_left(ant))
    numerator = (ant.left_antennax() - ant.posx) * FeltPheromone_left(ant) + (ant.right_antennax() - ant.posx) * FeltPheromone_right(ant)
    denom = FeltPheromone_left(ant) + FeltPheromone_right(ant)
    ant.forcex = numerator/denom

def ComputeForcey(ant):
    numer = (ant.left_antennay() - ant.posy) * FeltPheromone_left(ant) + (ant.right_antennay() - ant.posy) * FeltPheromone_right(ant)
    denom = FeltPheromone_left(ant) + FeltPheromone_right(ant)
    ant.forcey = numer/denom

each = 10

def Walk(ant):
    global i
    global each
    ant.posxold = ant.posx
    ant.posyold = ant.posy
    ant.velxold = ant.velx
    ant.velyold = ant.vely
    ComputeForcex(ant)
    ComputeForcey(ant)
    newvelx = ant.velxold + delta_t * (1./TAU)*(-ant.velxold + 1.*ant.forcex)
    newvely = ant.velyold + delta_t * (1./TAU)*(-ant.velyold + 1.*ant.forcey)
#    print('vel',newvely)
    newposx = ant.posxold + delta_t * newvelx
    newposy = ant.posyold + delta_t * newvely
    
    if newposx >= x_2 or newposx <= x_1:
        newposx = newposx + np.sign(x_2 - newposx)*(x_2-x_1)
    if newposy >= y_2 or newposy <= y_1:
        newposy = newposy + np.sign(y_2 - newposy)*(y_2-y_1)

    ant.posx = newposx
    ant.posy = newposy
    ant.velx = newvelx
    ant.vely = newvely

    if (i+1)%each == 0:
#        print('eeeee')
        droplet = Droplet(ant,0)
        AllThePheromone.append(droplet)


wn = Tk()
canvas = Canvas(wn, width = 600, height = 600)
canvas.pack()
toons = []
drops = []
dim = 5.
ballsize = 1.
scale=9.5
trans= 300

def canvas_coords(coords):
    global scale
    global trans
    return tuple([scale*p + trans for p in coords])


for i in range(NumberOfAnts):
    ball = AllTheAnts[i].posx, AllTheAnts[i].posy, AllTheAnts[i].posx+ballsize, AllTheAnts[i].posy+ballsize
    toons.append(canvas.create_oval(canvas_coords(ball),fill="blue"))


dim = 5.
iter = 5000

while True:
    for i in range(iter):
        CurrentTime = CurrentTime + delta_t
        for j in range(NumberOfAnts):
            Walk(AllTheAnts[j])
            ball = AllTheAnts[j].posx,AllTheAnts[j].posy,AllTheAnts[j].posx+ballsize,AllTheAnts[j].posy+ballsize
            ball = canvas_coords(ball)
            canvas.coords(toons[j],ball)
            if (i+1)%each == 0:
                canvas.create_oval(ball)
        AllThePheromone = AllThePheromone[-MaxActiveDropletsPerAnt:]
        canvas.update()
        print('iter = ',i,' Current time = ', CurrentTime, 'drops = ', len(AllThePheromone))




wn.mainloop()

#print(Heat(.5,0,20.))
#Angle(1,2)
#AngleBetween(1,2,3,4)
#print(AllTheAnts[3].vely)
#print(AllTheAnts[3].left_antennax())
#print(FeltPheromone_left(AllTheAnts[3]))
#
#drop = Droplet(AllTheAnts[3],1)
#drop.show()
#print([i.posx for i in AllTheAnts],"dede")

#wn.exitonclick()

