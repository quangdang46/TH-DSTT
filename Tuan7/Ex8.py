import numpy as np

def column_space(A,w):
    if len(A)!=len(w):
        return False
    if np.linalg.matrix_rank(A)<np.linalg.matrix_rank(np.array(A,w)):
        return False
    return True 
def is_null_space(A,w):
    if len(A)!=len(w):
        return False
    if np.dot(A,w)==0:
        return True
    return False

# A=np.array([[7, 6, -4, 1],[-5 ,-1 ,0 ,-2],[9, -11, 7, -3],[19 ,-9 ,7 ,1]])
# w=np.array([1,1,-1,-3])

A=np.array([[-8,-2,-9],[6,4,8],[4,0,4]])
w=np.array([2,1,-2]).T
# print(column_space(A,w))
# print(is_null_space(A,w))







