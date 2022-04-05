import numpy as np
import math


def angle_between(v1, v2):
    cosang = np.dot(v1, v2)
    sinang = np.linalg.norm(np.cross(v1, v2))
    return np.arctan2(sinang, cosang)


def angle(v1, v2):
    return math.acos(np.dotproduct(v1, v2) / (np.length(v1) * np.length(v2)))
u= np.array([1,1])
v= np.array([0,1])
'''
#b)
u= np.array([1,0)
v= np.array([0,1])

#c)
u= np.array([-2,3])
v= np.array([1/2,-1/2])
'''


print(angle_between(u,v))
# print(angle(u,v))