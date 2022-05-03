import numpy as np
A=np.array([[-2,2,-3],
            [2,1,-6],
            [-1,-2,0]])

# A
values,vectors=np.linalg.eig(A)
print("the eigenvalues of A\n",values)
print("the eigenvectors of A\n",vectors)
# A.T
values,vectors=np.linalg.eig(A.T)
print("the eigenvalues of A.T\n",values)
print("the eigenvectors of A.T\n",vectors)
# A^-1
values,vectors=np.linalg.eig(np.linalg.inv(A))
print("the eigenvalues of A^-1\n",values)
print("the eigenvectors of A^-1\n",vectors)