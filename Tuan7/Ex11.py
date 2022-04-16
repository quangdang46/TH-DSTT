import numpy as np
from sympy import *

#vector.T
M=np.array([[1,0,2],[0,1,-2],[2,4,-4]])
print("the dimendion: ",M.ndim)
c,pivot=Matrix.rref(Matrix(M.T))
print(c[pivot,:])
