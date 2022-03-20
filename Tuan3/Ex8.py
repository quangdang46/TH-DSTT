# Ex8
import numpy as np
A=np.array([[12,5,8],[15,9,12],[10,14,10],[16,7,9],[12,10,15]]).T
B=np.array([2,1,3]).reshape(3,1)
print(np.sum(A*B,axis=0))