import numpy as np
from sympy import *
def Hilbert_matrix(n):
    M=Matrix(np.zeros((n,n)))
    for i in range(n):
        for j in range(n):
            M[i,j]=1/(i+j+1)
    return M

def Pascal_matrix(n):
    C = [[0 for x in range(2 * n + 1)]
            for y in range(2 * n + 1)]
    for i in range(2 * n + 1):
        for j in range(min(i, 2 * n) + 1):

            if (j == 0 or j == i):
                C[i][j] = 1;

            else:
                C[i][j] = (C[i - 1][j - 1] +
                           C[i - 1][j]);
     
    M=np.zeros((n,n))    
    for i in range(n):
        for j in range(n):
            M[i][j] =C[i+j][j];
    return M
# pprint(Pascal_matrix(5))


def Magic_matrix(n):
    C = [[0 for x in range(n)]
                   for y in range(n)]

    i = n // 2
    j = n - 1
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
 
        if C[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            C[int(i)][int(j)] = num
            num = num + 1
 
        j = j + 1
        i = i - 1
    M=np.zeros((n,n))
    for i in range(0, n):
        for j in range(0, n):
            M[i][j] =C[i][j]
    return M

A=np.array(Hilbert_matrix(5))
B=np.array(Pascal_matrix(5))
C=np.array(Magic_matrix(5))
# a basis for the null space
print(A)
pprint(B)
pprint(C)
D=Matrix(A).nullspace()
E=Matrix(B).nullspace()
F=Matrix(C).nullspace()
def basis(M):
    c,pivot=Matrix.rref(M)
    #the bases of row
    print(c[pivot,:])

    c,pivot=Matrix.rref(M.T)
    #the bases of column
    print(c[:,pivot])

# basis(D)
# basis(E)
# basis(F)


