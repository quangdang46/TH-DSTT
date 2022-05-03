import numpy as np
# Find the singular values of the matrices
A1=np.array([[1,0],
            [0,-3]])
A2=np.array([[-5,0],
            [0,0]])
A3=np.array([[np.sqrt(6),1],
            [0,np.sqrt(6)]])
A4=np.array([[np.sqrt(3),2],
            [0,np.sqrt(3)]])
print("singular values of the matrices A1:",np.linalg.svd(A1,compute_uv=False))
print("singular values of the matrices A2:",np.linalg.svd(A2,compute_uv=False))
print("singular values of the matrices A3:",np.linalg.svd(A3,compute_uv=False))
print("singular values of the matrices A4:",np.linalg.svd(A4,compute_uv=False))
