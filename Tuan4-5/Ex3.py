from matplotlib import cm
# Exercise 3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

'''
#vo nghiem
a1 = 1
a2 = 2
b1 = 2
b2= 4
c1 = 3
c2 = 6
d1 = 50
d2 =500 
'''
'''
#co nghiem duy nhat
a1 = 1
a2 = 1
b1 = 1
b2= -1
c1 = -1
c2 = -2
d1 = 1
d2 = 1
'''
#vo so nghiem
a1 = 1
a2 = 1
b1 = -1
b2= -1
c1 = -1
c2 = -1
d1 = 1
d2 = 1

x, y = np.meshgrid(np.arange(-5, 5), np.arange(-5, 5))
# ax + by + cz = d => z = (d - ax - by )/c
z1 = (d1 - a1*x - b1*y)/c1
z2 = (d2 - a2*x - b2*y)/c2
fig = plt.figure()
ax = fig.add_subplot (111, projection = '3d')
ax.plot_surface(x, y, z1, cmap = plt.cm.ocean, alpha =0.4)
ax.plot_surface (x, y, z2, cmap = plt.cm.cool, alpha =0.7)
plt.show()