import numpy as np
def isDiagonalMatrix(mat) :
    for i in range(0, len(mat)):
        for j in range(0,len(mat)) :
            if ((i != j) and (mat[i][j] != 0)) :
                return False
    return True

A1=np.array([[4,-5],
            [2,-3]])
A2=np.array([[0,2],
            [0,1]])
A3=np.array([[2,3],
            [1,4]])
A4=np.array([[1,2,-2],
            [-2,5,-2],
            [-6,6,-3]])
A5=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])
if (isDiagonalMatrix(A1)) :
    print("A1 is diagonal")
else :
    print("A1 is not diagonal")
if (isDiagonalMatrix(A2)) :
    print("A2 is diagonal")
else :
    print("A2 is not diagonal")
if (isDiagonalMatrix(A3)) :
    print("A3 is diagonal")
else :
    print("A3 is not diagonal")
if (isDiagonalMatrix(A4)) :
    print("A4 is diagonal")
else :
    print("A4 is not diagonal")
if (isDiagonalMatrix(A5)) :
    print("A5 is diagonal")
else :
    print("A5 is not diagonal")