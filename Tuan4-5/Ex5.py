import numpy as np
A=np.array([[1,2,1], [2,2,2], [2,4,1]])
b=np.array([1,1,2])
#Option 1:
# print(np.linalg.solve(A,b.T))
#Option 2:
# print(np.linalg.inv(A)@b)
#Option 3:
D=np.linalg.det(A)
Dx=np.array([[1,2,1],[1,2,2],[2,4,1]])
Dy=np.array([[1,1,1],[2,1,2],[2,2,1]])
Dz=np.array([[1,2,1],[2,2,1],[2,4,2]])
x=np.linalg.det(Dx)/D
y=np.linalg.det(Dy)/D
z=np.linalg.det(Dz)/D
print([x,y,z])



