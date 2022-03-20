import numpy as np
import random
A=np.random.randint(1,10,size=(5,5))
B=np.random.randint(1,10,size=(5,5))
ans_A=np.linalg.det(A+B)
ans_B=np.linalg.det(A)+np.linalg.det(B)
print(ans_A)
print(ans_B)


for _ in range(3):
  n=random.randint(2,5)
  A=np.random.randint(1,10,size=(n,n))
  B=np.random.randint(1,10,size=(n,n))
  print(A)
  print(B)
  ans_A=np.linalg.det(A+B)
  ans_B=np.linalg.det(A)+np.linalg.det(B)
  print("det(A)=",ans_A)
  print("det(B)=",ans_B)
  if round(ans_A)!=round(ans_B):
    print('wrong')
  else:
    print('correct')
