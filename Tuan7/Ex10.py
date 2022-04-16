import numpy as np

# det(=0) phu thuoc tuyen tinh
# det(A) != 0 doc lap tuyen tinh
def is_linear_combination(M):
    Z=[0]*M.shape[0]
    if M.shape[0] != M.shape[1]:
        K=np.linalg.solve(M,np.array(Z))
        if len(K[K!=0])==0:
            print("linearly independent")
        else:
            print("linearly dependent")
    else:
        if(np.linalg.det(M)==0):
            print("not linearly independent")
        else:
            print("linearly independent")
            print(np.linalg.solve(M,np.array(Z)))

# a
M=np.array([[1,0,1],[-2,-4,-1],[0,1,1]])
print(is_linear_combination(M))
# b
np.array([[1,0,2],[0,1,-2],[2,4,-4]])
print(is_linear_combination(M))

# c
M=np.array([[0, 0, 1, 2, 3],[0, 0, 2, 3, 1],[1, 2, 3, 4, 5],[2, 1, 0, 0, 0],[-1, -3, -5, 0, 0]])
print(is_linear_combination(M))