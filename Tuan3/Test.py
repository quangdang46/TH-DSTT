import numpy as np
# random matrix
A=np.random.randint(1,10,size=(6,6))
print(A)
# tong phan tu duong cheo chinh
# print(np.trace(A))

A[1:-1,1:-1]=0
print(A)
# kiem tra ma tran doi
# det=np.linalg.det

