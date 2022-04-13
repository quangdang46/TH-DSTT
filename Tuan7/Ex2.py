import numpy as np
# orthogonal projection
def orthogonal_projection(A, B):
    return np.dot(A, B) / np.dot(B, B) * B
y=np.array([7,6])
u=np.array([4,2])
print(orthogonal_projection(y,u))
