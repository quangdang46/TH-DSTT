from sympy import * 
import numpy as np
A=Matrix([[1 ,0, 2, 3],[4,-1, 0, 2],[0,-1 ,-8, -10]])
# null space
M=A.nullspace()
v1,v2=M[0],M[1]
print(v1)
print(v2)
# Check to find if any linear combination of v1 and v2 is in M
v1=np.array(v1)
v2=np.array(v2)
v1=[k for k in v1]
print(v1)
# todo

















