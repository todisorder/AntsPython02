#import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation
from random import *
#from tkinter import *
#from tkinter import messagebox
#import turtle
import multiprocessing as mp
import time
start_time = time.time()





from file_to_be_read_by_python import *


Pi = np.pi


delta_t = delta_t / t_hat_in_seconds
CurrentTime = delta_t
#drop_every_seconds = .5
#drop_every_t_hat = drop_every_seconds / t_hat_in_seconds
def drop_or_not(time):
    return int(time/drop_every_t_hat) - int((time-delta_t)/drop_every_t_hat) == 1

#DropletAmount = DropletAmountPerUnitTime * drop_every_t_hat
print('will drop {:.3f} phero every {:.4f} t_hat.'.format(DropletAmount,drop_every_t_hat))


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
PreviousPheromone = []

def Angle(x,y):
    return np.arctan2(y,x)

def AngleBetween(x1,y1,x2,y2):
    dot = x1*x2 + y1*y2
    det = x1*y2 - y1*x2
    return  np.arctan2(det,dot)


seed(263232)

for i in range(NumberOfAnts):
    posx = random()*(x_2-x_1) + x_1
    posy = random()*(y_2-y_1) + y_1
    ia =random()*2.*Pi
    velx = np.cos(ia)*NaturalVelocity
    vely = np.sin(ia)*NaturalVelocity
    AllTheAnts[i] = Ant(posx,posy,velx,vely)                # Create the ants



def Heat(x,y,t):
    aux = (1. / (4.*Pi* Diffusion * t))
    aux *= np.exp(-(x*x + y*y) / (4.*Diffusion*t))
    aux *= np.exp(-Evaporation*t)
    aux *= DropletAmount
    return aux

def FeltPheromone_left(ant):
    result = []
    for ph in PreviousPheromone:
        x = ph.posx - ant.left_antennax()
        y = ph.posy - ant.left_antennay()
        t = CurrentTime - ph.origin_time
        result = result+[Heat(x,y,t)]
    return max(Threshold,sum(result))

def FeltPheromone_right(ant):
    result = []
    for ph in PreviousPheromone:
        x = ph.posx - ant.right_antennax()
        y = ph.posy - ant.right_antennay()
        t = CurrentTime - ph.origin_time
        result = result+[Heat(x,y,t)]
#        print('res ',result)
    return max(Threshold,sum(result))



#def ComputeForcex(ant):     # deprecated
#    numerator = (ant.left_antennax() - ant.posx) * FeltPheromone_left(ant) + (ant.right_antennax() - ant.posx) * FeltPheromone_right(ant)
#    denom = FeltPheromone_left(ant) + FeltPheromone_right(ant)
#    ant.forcex = numerator/denom
#
#def ComputeForcey(ant):     # deprecated
#    numer = (ant.left_antennay() - ant.posy) * FeltPheromone_left(ant) + (ant.right_antennay() - ant.posy) * FeltPheromone_right(ant)
#    denom = FeltPheromone_left(ant) + FeltPheromone_right(ant)
#    ant.forcey = numer/denom

def ComputeForce(ant):
    ax = ant.posx
    ay = ant.posy
    alx = ant.left_antennax()
    aly = ant.left_antennay()
    arx = ant.right_antennax()
    ary = ant.right_antennay()
    fpl = FeltPheromone_left(ant)
    fpr = FeltPheromone_right(ant)
    denom = fpl + fpr
    numerx = (alx - ax)*fpl + (arx - ax)*fpr
    Fx = numerx/denom
    numery = (aly - ay)*fpl + (ary - ay)*fpr
    Fy = numery/denom
    ant.forcex = Fx
    ant.forcey = Fy
#    print('I am feeling {},{} phero'.format(fpl,fpr))


save_every = 10

def Walk(ant,iter):
    global each
#    print('Calling Walk with iter =',iter)
    ant.posxold = ant.posx
    ant.posyold = ant.posy
    ant.velxold = ant.velx
    ant.velyold = ant.vely
    ComputeForce(ant)
    newvelx = ant.velxold + delta_t * (1./TAU)*(-ant.velxold + LambdaDeltas*ant.forcex)
    newvely = ant.velyold + delta_t * (1./TAU)*(-ant.velyold + LambdaDeltas*ant.forcey)
#    print('changed velocity from {} to {}'.format(ant.velyold,newvely))
    newposx = ant.posxold + delta_t * newvelx
    newposy = ant.posyold + delta_t * newvely
    
    if newposx >= x_2 or newposx <= x_1:
        newposx = newposx + np.sign(x_2 - newposx)*(x_2-x_1)
    if newposy >= y_2 or newposy <= y_1:
        newposy = newposy + np.sign(y_2 - newposy)*(y_2-y_1)
#    print('changed position from {} to {}'.format(ant.posx,newposx))

    ant.posx = newposx
    ant.posy = newposy
    ant.velx = newvelx
    ant.vely = newvely

#    if (iter+1)%each == 0:
##        print('eeeee')
#        droplet = Droplet(ant,0)
#        AllThePheromone.append(droplet)


    return [ant.posx,ant.posy]



toons = []
drops = []
dim = 5.
ballsize = 1.
scale=9.5
trans= 300


def on_press(event):
    if event.key.isspace():
        if animation.running:
            animation.event_source.stop()
        else:
            animation.event_source.start()
        animation.running ^= True


dim = 5.
#iter = 5000

fig = plt.figure()

#fig_phero = plt.figure()

ax = fig.add_axes([0, 0, 1, 1], frameon=True)
#ax_phero = fig_phero.add_axes([0, 0, 1, 1], frameon=True)

ax.set_xlim(x_1, x_2)
ax.set_ylim(y_1, y_2)
#ax_phero.set_xlim(x_1, x_2)
#ax_phero.set_ylim(y_1, y_2)

ax.set_aspect('equal')
#ax_phero.set_aspect('equal')

toons = np.zeros(NumberOfAnts, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('color',    float, 4)])


tail_length = 40
#tail = np.zeros(NumberOfAnts, dtype=[('x', float, tail_length),
#                                     ('y', float, tail_length)])
tailx = [[0.]*tail_length]*NumberOfAnts
taily = [[0.]*tail_length]*NumberOfAnts

for i in range(NumberOfAnts):
        tailx[i] = [AllTheAnts[i].posx]*tail_length
        taily[i] = [AllTheAnts[i].posy]*tail_length

drawing = ax.scatter(toons['position'][:,0],toons['position'][:,1])
drawing2 = [ax.scatter(tailx[j],taily[j],3) for j in range(NumberOfAnts)]
AllTails = [0.,0.]*NumberOfAnts

def AdvanceAnt(j,iter):
    global AllTheAnts
#    print('Calling AdvanceAnt with ant nr =',j,' iter = ',iter)
#    (AllTheAnts[j].posx,AllTheAnts[j].posy) = Walk(AllTheAnts[j],iter)
    return [j,Walk(AllTheAnts[j],iter)]

    
def AdvanceAnt2(j,iter):
    toons['position'][j][0] = AllTheAnts[j].posx
    toons['position'][j][1] = AllTheAnts[j].posy
    tailx[j].pop(0)
    tailx[j].append(AllTheAnts[j].posx)
    taily[j].pop(0)
    taily[j].append(AllTheAnts[j].posy)
    AllTails = [[tailx[j][k],taily[j][k]] for k in range(tail_length)]
    AllTails = np.array(AllTails)
#    print(AllTails)
    drawing2[j].set_offsets(AllTails)
    if (iter+1)%save_every == 0:
#        print("Wazzzup")
        save_this_ant(AllTheAnts[j],j)

#cores = mp.cpu_count()
#    cores=1
print('using {} cores'.format(Cores))


def update(iter):
    global CurrentTime
    global AllThePheromone
    global PreviousPheromone
    global AllTails
    global AllTheAnts
#    global cores
    CurrentTime = CurrentTime + delta_t
#    print('Calling update with iter =',iter)

    b = list(range(NumberOfAnts))
    
    pool = mp.Pool(Cores)

    c = [(i,iter) for i in b]
    d = [iter for i in b]
    

    result = pool.starmap(AdvanceAnt,[(j,iter) for j in b])
#    print(result)
    pool.close()
    
    each = drop_or_not(CurrentTime)
#    print('each = {:.3f}'.format(each))
    for j in [result[k][0] for k in range(len(result))]:
        AllTheAnts[j].posx = result[j][1][0]
        AllTheAnts[j].posy = result[j][1][1]
        if each:
            print('am dropping {} phero'.format(DropletAmount))
            droplet = Droplet(AllTheAnts[j],0)
            AllThePheromone.append(droplet)
            ax.scatter(droplet.posx,droplet.posy,s=20,c='c',alpha=0.2)




    for j in b:
        AdvanceAnt2(j,iter)


#    for j in b:
#        AdvanceAnt(j,iter)     # THIS WORKS.
#        AdvanceAnt2(j,iter)

#    for j in b:
#        AdvanceAnt(j,iter)     # THIS WORKS.

    drawing.set_offsets(toons['position'])

    AllThePheromone = AllThePheromone[-MaxActiveDropletsPerAnt:]
    PreviousPheromone = AllThePheromone
#    print('iter = ',iter,' Current time = ', CurrentTime, 'drops = ', len(PreviousPheromone))
    execution_time = time.time() - start_time
    print('--- {:.4f} seconds per iteration; {} iterations; {:.4f} time (sec); {} droplets---'.format(execution_time/(iter+1),iter,CurrentTime*t_hat_in_seconds,len(PreviousPheromone)),end='\r')

fig.canvas.mpl_connect('key_press_event', on_press)

def do_animation():
    global fig
    global update
    animation = FuncAnimation(fig,update)
    return animation

def save_this_ant(ant,j):
    filename = "hahahah-{:03d}.txt".format(j)
#    f = open(filename,"w").close()
    f = open(filename,"a")
    f.write("{:010f}\t{:010f}\n".format(ant.posx,ant.posy))
    f.close()


def save_ants(event=None):
    for j in range(NumberOfAnts):
        save_this_ant(AllTheAnts[j],j)


#axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
#axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
#bnext = Button(axnext, 'Next')
#bprev = Button(axprev, 'Previous')
#bnext.on_clicked(save_ants)

animation = do_animation()
animation.running = True
plt.show()

print('')




