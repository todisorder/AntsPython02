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
        self.stingposx = self.posx - SENSING_AREA_RADIUS*np.cos(Angle(self.velx,self.vely))
        self.stingposy = self.posy - SENSING_AREA_RADIUS*np.sin(Angle(self.velx,self.vely))

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
        self.posx = ant.stingposx
        self.posy = ant.stingposy
    def elapsed_time(self,CurrentTime):
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


save_every = 1000000000000

def Walk(ant,iter):
    global each
#    print('Calling Walk with iter =',iter)
#    print('velx is {}'.format(ant.velx))
    ant.posxold = ant.posx
    ant.posyold = ant.posy
    ant.velxold = ant.velx
    ant.velyold = ant.vely
#    print('velxold is {}'.format(ant.velxold))
    ComputeForce(ant)
    newvelx = ant.velxold + delta_t * (1./TAU)*(-ant.velxold + LambdaDeltas*ant.forcex)
    newvely = ant.velyold + delta_t * (1./TAU)*(-ant.velyold + LambdaDeltas*ant.forcey)
#    print('changed velocity from {} to {}'.format(ant.velyold,newvely))
    newposx = ant.posxold + delta_t * newvelx
    newposy = ant.posyold + delta_t * newvely
    
#    periodic:
#    if newposx >= x_2 or newposx <= x_1:
#        newposx = newposx + np.sign(x_2 - newposx)*(x_2-x_1)
#    if newposy >= y_2 or newposy <= y_1:
#        newposy = newposy + np.sign(y_2 - newposy)*(y_2-y_1)
#   lazy reflective
    newposx = max(x_1,min(x_2,newposx))
    if newposx >= x_2 or newposx <= x_1:
        newvelx = -newvelx
    newposy = max(y_1,min(y_2,newposy))
    if newposy >= y_2 or newposy <= y_1:
        newvely = -newvely


    ant.posx = newposx
    ant.posy = newposy
    ant.velx = newvelx
    ant.vely = newvely
#    print('velx is now {}'.format(ant.velx))
#    print('posx is now {}'.format(ant.posx))

#    if (iter+1)%each == 0:
##        print('eeeee')
#        droplet = Droplet(ant,0)
#        AllThePheromone.append(droplet)


    return [ant.posx,ant.posy,ant.velx,ant.vely]



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

droplet_drawing = ax.scatter([0],[0])
#droplet_drawing.remove()

for i in range(NumberOfAnts):
        tailx[i] = [AllTheAnts[i].posx]*tail_length
        taily[i] = [AllTheAnts[i].posy]*tail_length

drawing = ax.scatter(toons['position'][:,0],toons['position'][:,1])
drawing2 = [ax.scatter(tailx[j],taily[j],3) for j in range(NumberOfAnts)]
AllTails = [0.,0.]*NumberOfAnts

def AdvanceAnt(j,iter):
    global AllTheAnts
#    print('Calling AdvanceAnt with ant nr =',j,' iter = ',iter)
    return [j,Walk(AllTheAnts[j],iter)]

    
def DrawAntsAndTails(j,iter):
    toons['position'][j][0] = AllTheAnts[j].posx
    toons['position'][j][1] = AllTheAnts[j].posy
    tailx[j].pop(0)
    tailx[j].append(AllTheAnts[j].posx)
    taily[j].pop(0)
    taily[j].append(AllTheAnts[j].posy)
    AllTails = [[tailx[j][k],taily[j][k]] for k in range(tail_length)]
    AllTails = np.array(AllTails)
    drawing2[j].set_offsets(AllTails)
    drawing.set_offsets(toons['position'])
    if (iter+1)%save_every == 0:
#        print("Wazzzup")
        save_this_ant(AllTheAnts[j],j)


def DrawPheromone(j):
    global droplet_drawing
    how_many_droplets = len(AllThePheromone)
    drop_range = range(how_many_droplets)
    #    print('droplets are in number {}'.format(how_many_droplets))
    dropx = [AllThePheromone[j].posx for j in drop_range]
    dropy = [AllThePheromone[j].posy for j in drop_range]
#    drop_sizes = [500*np.sqrt(.1*AllThePheromone[j].elapsed_time(CurrentTime)) for j in drop_range]
#    drop_alpha = [np.exp(-AllThePheromone[j].elapsed_time(CurrentTime)) for j in drop_range]
    drop_sizes = [30 for j in drop_range]
    drop_alpha = [.3 for j in drop_range]
    colors_for_alpha = [[1,0,0,j*0.2] for j in  drop_alpha]
    droplet_drawing.remove()
    droplet_drawing = ax.scatter(dropx,dropy,s=drop_sizes,c=colors_for_alpha,edgecolors='none')




print('using {} cores'.format(Cores))

plot_exists = False
real_iter = 1
real_iter_each_iter = 25

def update(iter):

    global droplet_drawing
    global plot_exists
    global CurrentTime
    global AllThePheromone
    global PreviousPheromone
    global AllTails
    global AllTheAnts
    global real_iter
    global real_iter_each_iter

#    print('Calling update with iter =',iter)

    for ii in range(real_iter,real_iter + real_iter_each_iter):
#        print('doing calculation {} times'.format(ii))
        real_iter += 1
    
        this_iteration_timer = time.time()
        CurrentTime = CurrentTime + delta_t

        if Cores > 1:
            b = list(range(NumberOfAnts))
            pool = mp.Pool(Cores)
            result = pool.starmap(AdvanceAnt,[(j,iter) for j in b])
            pool.close()
            for j in [result[k][0] for k in range(len(result))]:
                AllTheAnts[j].posx = result[j][1][0]
                AllTheAnts[j].posy = result[j][1][1]
                AllTheAnts[j].velx = result[j][1][2]
                AllTheAnts[j].vely = result[j][1][3]

        else:
            b = list(range(NumberOfAnts))
            result = [AdvanceAnt(j,iter) for j in b]


        each = drop_or_not(CurrentTime)
        for j in [result[k][0] for k in range(len(result))]:
            if each:
    #            how_many_droplets = len(AllThePheromone)
    #            drop_range = range(how_many_droplets)
    #            #    print('droplets are in number {}'.format(how_many_droplets))
    #            dropx = [AllThePheromone[j].posx for j in drop_range]
    #            dropy = [AllThePheromone[j].posy for j in drop_range]
    #            drop_sizes = [1000*np.sqrt(.1*AllThePheromone[j].elapsed_time(CurrentTime)) for j in drop_range]
    #            drop_alpha = [np.exp(-AllThePheromone[j].elapsed_time(CurrentTime)) for j in drop_range]
    #            colors_for_alpha = [[1,0,0,j*0.2] for j in  drop_alpha]
    #
                AllTheAnts[j].stingposx = AllTheAnts[j].posx - SENSING_AREA_RADIUS*np.cos(Angle(AllTheAnts[j].velx,AllTheAnts[j].vely))
                AllTheAnts[j].stingposy = AllTheAnts[j].posy - SENSING_AREA_RADIUS*np.sin(Angle(AllTheAnts[j].velx,AllTheAnts[j].vely))
                droplet = Droplet(AllTheAnts[j],CurrentTime)
                AllThePheromone.append(droplet)
    #            droplet_drawing.remove()
    #            droplet_drawing = ax.scatter(dropx,dropy,s=drop_sizes,c=colors_for_alpha,edgecolors='none')
                plot_exists = True




        if True:
            for j in b:
                DrawAntsAndTails(j,iter)
                if each:
                    DrawPheromone(j)


        AllThePheromone = AllThePheromone[-MaxActiveDropletsPerAnt:]
        PreviousPheromone = AllThePheromone
    #    print('iter = ',iter,' Current time = ', CurrentTime, 'drops = ', len(PreviousPheromone))
        execution_time = time.time() - start_time
    #    print('--- {:.4f} seconds per iteration; {} iterations; {:.4f} time (sec); {} droplets---'.format(execution_time/(iter+1),iter,CurrentTime*t_hat_in_seconds,len(PreviousPheromone)),end='\r')
        print('--- Total exec time: {:.4f} sec for {} iterations; real time is {:.4f} sec'.format(execution_time,real_iter,CurrentTime),end='\r')
        this_iteration_total_time = time.time() - this_iteration_timer
#        print('--- {:.4f} in this iteration; {} iterations; {:.4f} time (sec); {} droplets---'.format(this_iteration_total_time,iter,CurrentTime*t_hat_in_seconds,len(PreviousPheromone)),end='\r')



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




