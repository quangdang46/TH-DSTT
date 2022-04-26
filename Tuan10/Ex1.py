import numpy as np
def Eigenvalues(Matrix):
    eigenvalues = np.linalg.eigvals(Matrix)
    return eigenvalues

# find det matrix buy eigenvalues
def Determinant(Matrix):
    eigenvalues = Eigenvalues(Matrix)
    det = 1
    for i in range(len(eigenvalues)):
        det *= eigenvalues[i]
    return det

A=np.array([[-1, 3.5, 14],
            [0, 5,-26],
            [0,0,2]])
B=np.array([[-2, 0, 0],
            [99, 0, 0],
            [10,-4.5,10]])

print("Eigenvalues of A:",Eigenvalues(A))
print("Det(A):",Determinant(A))
print("Eigenvalues of B:",Eigenvalues(B))
print("Det(B):",Determinant(B))
A=np.array([[5, 5, 0, 2],
            [0, 2, -3, 6],
            [0,0,3,-2],
            [0,0,0,5]])
B=np.array([[3, 0, 0, 0],
            [6, 2, 0, 0],
            [0, 3, 6, 0],
            [2,3,3,-5]])
C=np.array([[3, 0, 0 ,0, 0],
            [-5, 1, 0, 0, 0],
            [3, 8, 0, 0, 0],
            [0, -7, 2, 1, 0],
            [-4, 1, 9, -2, 3]])
print("Eigenvalues of A:",Eigenvalues(A))
print("Det(A):",Determinant(A))
print("Eigenvalues of B:",Eigenvalues(B))
print("Det(B):",Determinant(B))
print("Eigenvalues of C:",Eigenvalues(C))
print("Det(C):",Determinant(C))