import numpy as np
from sympy import *
# a)
A=np.array([[1,2,1],[2,-1,1],[2,1,0]])
B=np.array([0,0,0])
X = np.linalg.solve(A,B.T)
print(X)
# b)
A=np.array([[2,1,1,1],[1,2,1,1],[1,1,2,2],[1,1,1,2]])
B=np.array([1,1,1,1])
X = np.linalg.solve(A,B.T)
print(X)

'''
#option 2
ans_2=np.linalg.inv(A)@B
#option 3
D=np.linalg.det(A)
Dx=np.array([[0,2,1],[0,-1,1],[0,1,0]])
Dy=np.array([[1,0,1],[2,0,1],[2,0,0]])
Dz=np.array([[1,2,0],[2,-1,0],[2,1,0]])
x=np.linalg.det(Dx)/D
y=np.linalg.det(Dy)/D
z=np.linalg.det(Dz)/D
#option 4
M=Matrix([[1,2,1,0],[2,-1,1,0],[2,1,0,0]])
ans_4,pivot=M.rref()
'''
# M=Matrix([[1,2,1,0],[2,-1,1,0],[2,1,0,0]])
# ans_4,pivot=M.rref()
# print(ans_4)



