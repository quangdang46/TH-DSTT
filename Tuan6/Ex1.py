import numpy as np
def norm_1(mt):
    return np.sum(np.abs(mt))
A1=np.array([1,-7,-2,-3]).reshape(2,2)
A2=np.array([2,-8,3,1]).reshape(2,2)
A3=np.array([-2,8,3,1]).reshape(2,2)
A4=np.array([2,3,1,1]).reshape(2,2)
print(norm_1(A1))
print(norm_1(A2))
print(norm_1(A3))
print(norm_1(A4))



    