import numpy as np
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



def nghich_dao(mt):

    d_mt = dinh_thuc(mt)
    if d_mt == 0:        
        return None        

    so_hang = mt.shape[0]
    so_cot =  mt.shape[1]

    c = np.zeros(shape=( so_hang, so_cot))
    i = 0
    while i < so_hang:
        
        j = 0
        while j  < so_cot:
            pds = ma_tran_con(mt, i, j)
            c[i][j] = ((-1) ** (i + j)) * dinh_thuc(pds)
            j = j + 1
            pass
        i = i + 1
        pass

    k = -1 / d_mt
    c_t = c.transpose()
    ket_qua = np.multiply(c_t, k)
    return ket_qua




