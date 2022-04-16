import numpy as np
# orthogonal projection
# hình chiếu A lên B
def orthogonal_projection(A, B):
    return (sum(A*B) /sum(B*B)) * B
y=np.array([7,6])
u=np.array([4,2])
print(orthogonal_projection(y,u))
