import numpy as np
from sympy import *
A = np.array([[0.61, 0.29, 0.15], [0.35, 0.59, 0.063], [0.04, 0.12, 0.787]])
x,y,z=symbols('x,y,z')
b=np.array([x,y,z])
# b=np.array([1,2,3])

print(np.linalg.inv(A)@b)