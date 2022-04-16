import numpy as np
u1=np.array([3,1,1])
u2=np.array([-1,2,1])
u3=np.array([-1/2,2,7/2])
# vuông góc
def is_orthogonal(u1,u2,u3):
    if sum(u1*u2)==0 and sum(u1*u3)==0 and sum(u2*u3)==0:
        return True
    return False
print("u1,u2,u3 are orthogonal",is_orthogonal(u1,u2,u3))

