import numpy as np
# Find the singular values of the matrices
A1=np.array([[-18,13,-4,4],
            [2,29,-4,12],
            [-14,11,-12,8],
            [-2,21,4,8]])
A2=np.array([[6 ,-8 ,-4, 5, -4],
            [2, 7, -5, -6, 4],
            [0, -1,-8, 2,2],
            [-1, -2, 4, 4, -8]])

print("singular values of the matrices A1:",np.linalg.svd(A1,compute_uv=False))
print("singular values of the matrices A2:",np.linalg.svd(A2,compute_uv=False))
