import numpy as np
from math import sqrt
n=int(input("Nhap so phan tu cua mang: "))
b=np.array(range(12,12+2*n,2))
c=np.array(range(31,31+2*n,2))
x=np.array(range(-n,n+1))
y=np.array(range(n,-n-1,-1))
z=np.array(range(10,10-2*n,-2))
w=1/2**np.arange(0,n+1)
d=1/np.array([int(np.round((((1 + sqrt(5)) / 2)**i/np.sqrt(5)))) for i in range(1,n+1)])


# h
list_bool = [True] *100001
list_bool[0]=list_bool[1]=False
for i in range(2,int(sqrt(100000))):
    if list_bool[i]:
        for j in range(i*i,len(list_bool),i):
            list_bool[j]=False
list_prime=[]
for i in range(2,len(list_bool)):
    if list_bool[i]:
        list_prime.append(i)
print(np.array([1/list_prime[i] for i in range(n)]))

if n==0:a=[]
else:    
    a=[1]
    k=2
    for i in range(1,n):
        a.append(a[i-1]+k)
        k+=1


# n
if n==0:z=[]
else:    
    z=[2]
    k=3
    for i in range(1,n):   
        z.append(z[i-1]+k)
        k+=2
z=[1/k for k in z]

p=[i/(i+1) for i in range(n)]
o=[chr(i) for i in range(97,123)]
s=[chr(i) for i in range(65,91,3)]


