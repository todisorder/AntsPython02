import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D





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

    result = []
    part1 = 0.
    part2 = 0.
    part3 = 0.
    mx = mean(x)
    my = mean(y)
#    print('Computing correlation...')
    xmx = [k-mx for k in x]
    
    for i in range(1*len(x)):
        
        ymy = [k-my for k in StartsAtI(y,i)]
        
        result+=[InnerProd(xmx,ymy) / (Norm(xmx)*Norm(ymy))]

    return result

figcounter = 1

def ComputeCorrelation(dirlist):
    global figcounter
    fignum=figcounter
    ants = 25
    x=list(range(ants))
    y=list(range(ants))
    

    coords = [posx, velx, posy, vely, angle] = [0,1,2,3,4]
    
    #dirname = 'LastResult'
#    dirname = 'phero'
    NrOfDirs = len(dirlist)
    
    for dirnr in range(NrOfDirs):
        dirname = dirlist[dirnr]

        for i in range(ants):
            
            filename = dirname+'/AntPhase-'+str(i+1)+'.txt'
            with open(filename) as f:
                x[i],y[i] = np.loadtxt(f, delimiter=';', usecols=(posx,posy),  unpack=True)


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

        plt.figure(fignum)

        plt.subplot(1,NrOfDirs,dirnr+1)
        plt.ylabel(dirname)
        plt.imshow(CorrPortraitz)
    fignum = fignum+1

    figcounter=fignum
    print(figcounter)
    plt.draw()


##################################################################


#dirs = ['phero','nophero']
dirs = ['random w phero','random no phero']
ComputeCorrelation(dirs)
#ComputeCorrelation(['phero'])
#ComputeCorrelation(['nophero'])

plt.show()




