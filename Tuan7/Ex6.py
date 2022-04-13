import numpy as np
# linear combination of three vectors
def isLinearCombination(v1, v2, v3,w):
    if len(w)!=len(v1):
        return False
    if np.linalg.matrix_rank(np.array([v1, v2, v3]))<np.linalg.matrix_rank(np.array([v1, v2, v3,w])):
        return False
    return True     
# a   
v1 = np.array([1, 2, 3, 4])
v2 =np.array([-1, 0, 1, 3])
v3 =np.array([0, 5, -6, 8])
w =np.array([3, -6, 17, 11])
print(isLinearCombination(v1, v2, v3,w))

#b
v1 = np.array([1, 1, 2, 2])
v2 =np.array([2, 3, 5, 6])
v3 =np.array([2, -1, 3, 6])
w =np.array([0, 5, 3, 0])
print(isLinearCombination(v1, v2, v3,w))
# c
v1 = np.array([1, 1, 2, 2])
v2 =np.array([2, 3, 5, 6])
v3 =np.array([2, -1, 3, 6])
w =np.array([-1, 6, 1, -4])
print(isLinearCombination(v1, v2, v3,w))


def isLinearCombination(v1, v2, v3,v4,w):
    if len(w)!=len(v1):
        return False
    if np.linalg.matrix_rank(np.array([v1, v2, v3,v4]))<np.linalg.matrix_rank(np.array([v1, v2, v3,v4,w])):
        return False
    return True 
# d
v1 = np.array([1, 2, 3, 4])
v2 =np.array([-1, 0, 1, 3])
v3 =np.array([0, 5, -6, 8])
v4 =np.array([1, 15, -12, 8])
v4 =np.array([3, -6, 17, 11])

print(isLinearCombination(v1, v2,v3,v4,w))


