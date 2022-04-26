import numpy as np
from sympy import *
import matplotlib.pyplot as plt
x,y=symbols('x,y')
def ma_tran_con(mt, i, j):
    mtc = mt.copy()
    # xoa hang i 0
    mtc = np.delete(mtc, i, 0);
    # xoa cot j 1
    mtc = np.delete(mtc, j, 1); 
    return mtc

def dinh_thuc(mt):
    so_chieu = mt.shape[1]
    if so_chieu == 1==mt.shape[0]:
        return mt[0][0]
    elif mt.shape[0] != so_chieu:
        return None
    
    ket_qua = 0
    j = 0
    for i in range(so_chieu):
        # Tinh theo hang 0
        pds = ma_tran_con(mt, 0, j)
        ket_qua += ((-1) ** j) * mt[0][j] * dinh_thuc(pds)
        j = j + 1
    return ket_qua  

def Eigenvalues(Matrix):
    list_set=[32, 31.9, 31.8, 32.1, 32.2]
    for element in list_set:
        eigenvalues = np.linalg.eigvals(Matrix)
        print("Eigenvalues of A:",eigenvalues)
def characteristic(Matrix):
    list_set=[32, 31.9, 31.8, 32.1, 32.2]
    for element in list_set:
        Matrix[2][1]=element
        M=(Matrix-x*np.identity(len(Matrix)))
        print("Characteristic of A:",dinh_thuc(M))
# def Graphics(Matrix):
#     list_set=[32, 31.9, 31.8, 32.1, 32.2]
#     for element in list_set:
#         Matrix[2][1]=element
#         M=(Matrix-x*np.identity(len(Matrix)))
#         x1=np.linspace(1,3,10)
#         plt.plot(x1,dinh_thuc(M))        

#         plt.show()
        


    





A=np.array([[-6,28,21],
            [4,-15,-12],
            [8,y,25]])

# Eigenvalues(A)

characteristic(A)