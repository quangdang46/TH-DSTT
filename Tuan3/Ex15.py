import numpy as np
A=np.array([[2,4,5],[-3/4,2,1/4],[1/4,1/2,2]])
B=np.array([[1,-1/2,3/4],[3/2,1/2,-2],[1/4,1,1/2]])
print(np.dot(np.linalg.inv(A),np.linalg.inv(B)))
print()

print(np.linalg.inv(np.dot(A,B)))
print()

print(np.linalg.inv(np.dot(B,A)))
print()

print(np.linalg.inv(A).T)
print()

print(np.linalg.inv(A.T))