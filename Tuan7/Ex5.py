import numpy as np
from sympy import *
M=Matrix(np.array(
                [[1,0,2,3],
                [4,-1,0,2],
                [0,-1,-8,-10]]
                ))
# find bases of row space of matrix
c,pivot=Matrix.rref(M)
#the bases of row
print(c[pivot,:])



# find bases of column space of matrix
c,pivot=Matrix.rref(M.T)
#the bases of column
print(c[:,pivot])


# nullspace
print(M.nullspace())





