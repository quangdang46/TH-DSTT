# import numpy as np
from sympy import *
x,y,z,t=symbols('x y z t')
print(solve([Eq(2*x-4*y+4*z+0.077*t,3.86),Eq(-2*y+2*z-0.056*t,-3.47),Eq(2*x-2*y,0)]))
# A=np.array([[2,-4,4,0.077],[0,-2,2,-0.056],[2,-2,0,0]])
# b=np.array([3.86,-3.47,0])


# print(np.linalg.solve(A,b.T))
# M=Matrix([[2,-4,4,0.077,3.86],[0,-2,2,-0.056,-3.47],[2,-2,0,0,0]])
# ans,pivot=M.rref()
# print(ans)
