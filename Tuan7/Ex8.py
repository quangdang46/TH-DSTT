import numpy as np

def column_space(A,w):
    if len(A)!=len(w):
        return False
    if np.linalg.matrix_rank(np.array(A))<np.linalg.matrix_rank(np.array([A[0],A[1],A[2],A[3],w])):
        return False
    return True 
def is_null_space(A,w):
    if len(A)!=len(w):
        return False
    if np.sum(np.array(A)*np.array(w))==0:
        return True
    return False
def main(A,w):
    if column_space(A,w) and is_null_space(A,w):
        print("The null space and the column space are the same.")
    elif column_space(A,w) and not is_null_space(A,w):
        print("The null space is not the same as the column space.")
    elif not column_space(A,w) and is_null_space(A,w):
        print("The column space is not the same as the null space.")
    else:
        print("The null space and the column space are not the same.")

# A=np.array([[7, 6, -4, 1],[-5 ,-1 ,0 ,-2],[9, -11, 7, -3],[19 ,-9 ,7 ,1]])
# w=np.array([1,1,-1,-3])
A=[[7, 6, -4, 1],[-5 ,-1 ,0 ,-2],[9, -11, 7, -3],[19 ,-9 ,7 ,1]]
w=[1,1,-1,-3]
main(A,w)

# print(np.linalg.matrix_rank(np.array([A,w])))


A=np.array([[-8, 5, -2, 0],
            [-5, 2, 1, -2],
            [10, -8, 6,-3],
            [3, -2, 1, 0]])
A=[[-8, 5, -2, 0],
            [-5, 2, 1, -2],
            [10, -8, 6,-3],
            [3, -2, 1, 0]]
# w=np.array([1,2,1,0]).T
w=[1,2,1,0]
main(A,w)






