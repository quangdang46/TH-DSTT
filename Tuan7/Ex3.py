import numpy as np
from math import *
# np.set_printoptions(suppress=True)
def orthonormal_columns(A):
    return (np.round(A.T@A)==np.identity(A.shape[0])).all()
y=np.array([[cos(30),-sin(30)],[sin(30),cos(30)]])
print(orthonormal_columns(y))