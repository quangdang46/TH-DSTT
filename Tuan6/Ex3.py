import numpy as np
def  Frobenius_norm(mt):
    return np.sqrt(np.sum(np.square(mt)))

C1=np.array([-5,-4,2,-1,2,3,-2,1,0]).reshape(3,3)
C2=np.array([1,7,3,4,-2,-2,-2,-1,1]).reshape(3,3)

print(Frobenius_norm(C1))
print(Frobenius_norm(C2))