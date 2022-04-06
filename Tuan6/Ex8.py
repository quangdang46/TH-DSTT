import numpy as np
from math import *
A= np.array([[3,4,5],[1,3,1],[1,1,2]])
LT=[chr(i) for i in range(ord('A'),ord('Z')+1)]
LT.append(' ')
D=[]
str=input()
shift=int(input())
# xem moi phan tu la 1 ki tu phai thoai man kich thuoc ma tran D=MxN=len(str)
if int(len(str)/A.shape[1])*A.shape[1]!=len(str):
    print('Error')
    exit()
dict_LT=dict(zip(LT,range(1+shift,len(LT)+1+shift)))
for key in str:
    D.append(dict_LT[key])
D=np.array(D).reshape(A.shape[1],int(len(str)/A.shape[1]))
E=A@D
print(E)