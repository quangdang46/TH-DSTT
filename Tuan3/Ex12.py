import numpy as np
A = np.array([6, 0, 0, 5, 1, 7, 2, -5, 2, 0, 0, 0, 8, 3, 1, 8]).reshape(4, 4)
B = np.array([1, -2, 5, 2, 0, 0, 3, 0, 2, -6, -7, 5, 5, 0, 4, 4]).reshape(4, 4)
C = np.array([3, 5, -8, 4, 0, -2, 3, -7, 0, 0, 1, 5,  0, 0, 0, 2]).reshape(4, 4)
D = np.array([4, 0, 0, 0, 7, -1, 0, 0, 2, 6, 3, 0, 5, -8, 3, 0, 5, -8, 4, -3]).reshape(5, 4)#ma tran khong vuong
E = np.array([4, 0, -7, 3, -5, 0, 0, 2, 0, 0,  7, 3, -6, 4, -8,  5, 0, 5, 2, -3,  0, 0, 9, -1, 2]).reshape(5, 5)
F = np.array([6, 3, 2, 4, 0,  9, 0, -4, 1, 0,  8, -5, 6, 7, 1,  3, 0, 0, 0, 0, 4, 2, 3, 2, 0]).reshape(5, 5)
print(np.linalg.det(A))
print(np.linalg.det(B))
print(np.linalg.det(C))
# khong tinh duoc vi ma tran khong vuong
# print(np.linalg.det(D))
print(np.linalg.det(E))
print(np.linalg.det(F))