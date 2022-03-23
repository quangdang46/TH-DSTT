import matplotlib.pyplot as plt
import numpy as np
'''
#co nghiem duy nhat
a1=2
b1=-1
c1=1
a2=-40
b2=2
c2=-2
'''
'''
#vo nghiem
a1=2
b1=-1
c1=7
a2=6
b2=-3
c2=3
'''
#vo so nghiem
a1=1
b1=2
c1=3
a2=2
b2=4
c2=6
x=np.arange(-10,10)
y1=(c1-a1*x)/b1
y2=(c2-a2*x)/b2
fig=plt.figure()
plt.plot(x,y1,'r')
plt.plot(x,y2,'b')
plt.show()