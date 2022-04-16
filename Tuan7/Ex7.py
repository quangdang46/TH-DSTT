from sympy import * 
import numpy as np
A=Matrix([[1 ,0, 2, 3],[4,-1, 0, 2],[0,-1 ,-8, -10]])
# null space
M=A.nullspace()
v1,v2=M[0],M[1]
v1=list(v1)
v2=list(v2)
print(v1)
print(v2)
M_null=[v1,v2]
print(M_null)
# a,b=symbols('a b')
# A2LC=A*Matrix([[a*v1[0]-b*v2[0]],[a*v1[1]-b*v2[1]],[a*v1[2]-b*v2[2]]])
# print(A2LC)



