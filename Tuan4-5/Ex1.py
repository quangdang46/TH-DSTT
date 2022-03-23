import numpy as np
# a)
A=np.array([[1,2,1],[2,-1,1],[2,1,0]])
B=np.array([0]*3)
X = np.linalg.solve(A,B)
print(X)
# b)
A=np.array([[2,1,1,1],[1,2,1,1],[1,1,2,2],[1,1,1,2]])
B=np.array([1]*4)
X = np.linalg.solve(A,B)
print(X)

