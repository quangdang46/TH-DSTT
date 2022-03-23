'''
3x1-x3=0
8x1-2x4=0
2x2-2x3-x4=0
'''
from sympy import *
x1,x2,x3,x4=symbols('x1,x2,x3,x4')
# k=solve([Eq(3*x1-x3,0),Eq(8*x1-2*x4,0),Eq(2*x2-2*x3-x4,0)])
# print(type(k))
print(solve([Eq(3*x1-x3,0),Eq(8*x1-2*x4,0),Eq(2*x2-2*x3-x4,0)]))

