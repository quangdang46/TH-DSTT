import numpy as np
def Euclidean_distances(s1,s2):
    return np.sqrt(np.sum((s1-s2)**2))

v1= np.array([1,2,3]).T
s2= np.array([7,4,3]).T
s3= np.array([2,1,9]).T

print(Euclidean_distances(v1,s2))
print(Euclidean_distances(v1,s3))
print(Euclidean_distances(s2,s3))