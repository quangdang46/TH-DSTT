import numpy as np
A=np.array([[0.25,0.15,0.1], [0.4,0.15,0.2], [0.15,0.2,0.2]])
d=np.array([100,100,100]).T
I=np.array([[1,0,0],[0,1,0],[0,0,1]])
print(np.linalg.solve(I-A,d))