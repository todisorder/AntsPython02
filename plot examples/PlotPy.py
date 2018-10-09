import matplotlib.pyplot as plt
import numpy as np
x, y = np.loadtxt('LastResult/exp.txt', delimiter='	', unpack=True)
plt.plot(x,y, label='ok')
plt.show()