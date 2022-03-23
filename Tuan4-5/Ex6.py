
import numpy as np
A=np.array([[1,1,1], [1,2,4], [1,3,9]])
b=np.array([6,15,38])
print(np.linalg.solve(A,b.T))