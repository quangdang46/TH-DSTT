import numpy as np

def unit_vector(vector):
    # norm 2
    return vector / np.linalg.norm(vector)

a= np.array([2,3]).T
b= np.array([1,2,3]).T
c= np.array([1/2,-1/2,1/4]).T
d= np.array([np.sqrt(2),2,-np.sqrt(2)]).T
print(unit_vector(a))
print(unit_vector(b))
print(unit_vector(c))
print(unit_vector(d))
