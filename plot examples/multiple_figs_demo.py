"""
==================
Multiple Figs Demo
==================

Working with multiple figure windows and subplots
"""
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)

###############################################################################
# Create figure 1

plt.figure(1)
plt.subplot(211)
plt.plot(t, s1)
plt.subplot(212)
plt.plot(t, 2*s1)

###############################################################################
# Create figure 2

plt.figure(2)
plt.plot(t, s2)

###############################################################################
# Now switch back to figure 1 and make some changes

plt.figure(1)
plt.subplot(211)
plt.plot(t, s2, 's')
ax = plt.gca()
ax.set_xticklabels([])

plt.show()


data = 2 * np.random.random((10, 10))
data2 = 3 * np.random.random((10, 10))
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
from matplotlib.cbook import get_sample_data
img = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))


'''
    ======================
    3D surface (color map)
    ======================
    
    Demonstrates plotting a 3D surface colored with the coolwarm color map.
    The surface is made opaque by using antialiased=False.
    
    Also demonstrates using the LinearLocator and custom formatting for the
    z axis tick labels.
    '''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')   # gca = get current axes

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

############################################################

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()

X=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Y= [0,2500,5000,7500,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000]
Xm, Ym = np.meshgrid(X, Y)
Zmatrix=np.random.rand(len(Y),len(X))

ax = Axes3D(plt.gcf())      # gcf = get current figure
ax.plot_surface(Xm, Ym, Zmatrix)