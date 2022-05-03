import numpy as np
# A=np.array([[1,2,-2],
#             [0,3,-2],
#             [0,0,1]])

A=np.array([[2,0,0],
            [1,2,1],
            [-1,0,1]])
values,vectors=np.linalg.eig(A)
print("the eigenvalues of A\n",values)
print("the eigenvectors of A\n",vectors)



P=np.zeros((3,3))
for i in range(3):
    P[i,i]=np.diag(A)[i]

D=np.linalg.inv(P)@A@P
print("Solve\n",D)

