import numpy as np
def infinity_norm(mt):
    return np.max(np.abs(mt))
B1=np.array([1,-7,-2,-3]).reshape(2,2)
B2=np.array([3,6,1,0]).reshape(2,2)
B3=np.array([5,-4, 2,-1, 2, 3,-2, 1, 0]).reshape(3,3)
B4=np.array([3,6,-1,3,1,0,2,4,-7]).reshape(2,5)
print(infinity_norm(B1))
print(infinity_norm(B2))
print(infinity_norm(B3))
print(infinity_norm(B4))

