# Ex10
import numpy as np
A=np.array([-1,4,8,-9,1,2]).reshape(2,3)
B=np.array([5,8,0,-6,5,6]).reshape(3,2)
C=np.array([-4,1,6,5]).reshape(2,2)
D=np.array([-6,3,1,8,9,-2,6,-1,5]).reshape(3,3)
#TH KHONG NHAN DUOC
# print(np.dot(A,B.T))
print((D.T).T)
#TH KHONG NHAN DUOC
# print(2*A.T-5*B.T)
print(np.dot(C.T,C.T))
print(np.dot(B,C.T))
print(2*C.T)
print((-D).T)
print(C-C.T)
print(B+A.T)
print(-D.T)
print(D-D.T)
print((A.T+B).T)
print(np.dot(C,C).T)