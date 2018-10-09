import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#with open('LastResult/AntPhase-1.txt') as f:
#    a = np.loadtxt(f, delimiter=';',  usecols=(0,1,2), unpack=True)
#
#plt.plot(a[0],a[1], 'o',label='ok')
#plt.plot(a[0],a[2], 'o',label='ok')
#plt.show()



#mesma coisa:
with open('LastResult/AntPhase-1.txt') as f:
    x,y = np.loadtxt(f, delimiter=';', usecols=(0,2),  unpack=True)

#plt.plot(x,y, 'ro',label='ok')
#plt.show()

#plt.plot([1,2,3,4],'ro')
#plt.ylabel('some numbers')
#plt.show()


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def StartsAtI(a,I):
    result = []
    for i in range(len(a)):
        result.append(a[(i+I)%len(a)])
    return result

def InnerProd(a,b):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i]
    return sum

def Norm(a):
    return np.sqrt(InnerProd(a,a))

def Shorten(a,n):
    return [a[n*i] for i in range(int(len(a)/n))]



def correlation(x,y):
#    print(x)
#    print(y)

    result = []
    part1 = 0.
    part2 = 0.
    part3 = 0.
    mx = mean(x)
    my = mean(y)
    print('Computing correlation...')
    xmx = [k-mx for k in x]
    
    for i in range(1*len(x)):
        
        ymy = [k-my for k in StartsAtI(y,i)]
        
        result+=[InnerProd(xmx,ymy) / (Norm(xmx)*Norm(ymy))]

    return result



a=[1,2,10,3]
b=[1,2,10,3]


a=range(20)
b=StartsAtI(a,0)

#print(a)
#print(StartsAtI(a,0))
#print(StartsAtI(a,1))
#print(StartsAtI(a,2))
#print(StartsAtI(a,3))
#print(StartsAtI(a,18))



cc = correlation(a,b)
#print(correlation(a,b));
#plt.plot(cc,'r')
#plt.show()


ants = 10
x=list(range(ants))
y=list(range(ants))

coords = [posx, velx, posy, vely, angle] = [0,1,2,3,4]

#dirname = 'LastResult'
dirname = 'phero'

for i in range(ants):

    filename = dirname+'/AntPhase-'+str(i+1)+'.txt'
    with open(filename) as f:
        x[i],y[i] = np.loadtxt(f, delimiter=';', usecols=(posx,posy),  unpack=True)
#        x[i] = np.loadtxt(f, delimiter=';', usecols=0,  unpack=True)
#        y[i] = np.loadtxt(f, delimiter=';', usecols=1,  unpack=True)

#print(y[0])
#print(x[0])
#filename = 'LastResult/AntPhase-1.txt'
#with open(filename) as f:
#    x1 = np.loadtxt(f, delimiter=';', usecols=(0,),  unpack=True)
#
#filename = 'LastResult/AntPhase-2.txt'
#with open(filename) as f:
#    x2 = np.loadtxt(f, delimiter=';', usecols=(0,),  unpack=True)

#cc=range(25)
#cc=[0 for c in cc]
#for i in range(5):
#    for j in range(5):

#CorrPortraitx = list(range(ants))
#CorrPortraity = list(range(ants))
#CorrPortraitx, CorrPortraity = np.meshgrid(CorrPortraitx,CorrPortraity)
#CorrPortraitz = 0. * CorrPortraitx       # works bcause CorrPortraitx is now an array?...

#floor = np.arange(ants*ants).reshape((ants,ants))
floor = np.array([[0.]*ants]*ants)
CorrPortraitz = np.array([[0.]*ants]*ants)
AnotherCorrPortraitz = np.array([[0.]*ants]*ants)

for i in range(len(CorrPortraitz)):
    CorrPortraitz[i][i]=1.
    AnotherCorrPortraitz[i][i]=1.

nn = 10      # reduce size of list by nn for speed
print(range(ants))
for i in range(ants):
    for j in range(i+1,ants):
        print('(i,j) = (',i,',',j,')')
        xi = Shorten(x[i],nn)
        yi = Shorten(y[i],nn)
        xj = Shorten(x[j],nn)
        yj = Shorten(y[j],nn)
        cx = correlation(xi,xj)
        cy = correlation(yi,yj)
        maxcx = max(cx)
        maxcy = max(cy)
        CorrPortraitz[i][j] = maxcx*maxcy
        AnotherCorrPortraitz[i][j] = maxcy

plt.figure(1)
ax = plt.subplot(121)
plt.ylabel('maxcx*maxcy')
ax.imshow(CorrPortraitz)

ax = plt.subplot(122)
plt.ylabel('only maxcy')
ax.imshow(AnotherCorrPortraitz)

plt.show()


#plt.show()




