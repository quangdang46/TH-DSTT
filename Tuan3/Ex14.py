import numpy as np
import random
A=np.random.randint(1,10,size=(5,5))
B=np.random.randint(1,10,size=(5,5))
ans_A=np.linalg.det(A)*np.linalg.det(B)
ans_B=np.linalg.det(np.dot(A,B))
print(ans_A)
print(ans_B)


for _ in range(4):
  n=random.randint(2,5)
  A=np.random.randint(1,10,size=(n,n))
  B=np.random.randint(1,10,size=(n,n))
  print(A)
  print(B)
  ans_A=round(np.linalg.det(A)*np.linalg.det(B))
  ans_B=round(np.linalg.det(np.dot(A,B)))
  print("det(A)=",ans_A)
  print("det(B)=",ans_B)
  if ans_A!=ans_B:
    print('wrong')
  else:
    print('correct')
