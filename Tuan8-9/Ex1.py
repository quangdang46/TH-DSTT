import numpy as np
A=np.array([[2,2],[2,3]])
b=np.array([[4],[6]])
def solve(A,b):
    return np.linalg.solve(A.T@A,A.T@b)
print(solve(A,b))
