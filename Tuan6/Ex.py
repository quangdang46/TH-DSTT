import numpy as np
# def norm_1(mt):
#     return np.sum(np.abs(mt))

# def norm_2(mt):
#     return np.sqrt(np.sum(np.square(mt)))

# def infinity_norm(mt):
#     return np.max(np.abs(mt))

# w=np.array([-1,-2,1,4])
# print(norm_1(w))
# print(norm_2(w))
# print(infinity_norm(w))
# norm 1:1
# norm 2:2
# mac dinh la norm 2
# vo cung np.inf


'''

norm 1 max tổng cột
norm 2 căn tổng bình phương tình phần tử
vô cùng max tổng hàng
'''
A=np.array([1,-7,-2,-3,4,5,6,7]).reshape(2,4)

# norm 1 max tổng cột
# print(np.linalg.norm(A,1))
# print(np.max(np.sum(np.abs(A),axis=0)))

# norm 2 căn tổng bình phương tình phần tử
print(np.linalg.norm(A,'fro'))
print(np.sqrt(np.sum(np.square(A))))
# norm infinity max tổng hàng
print(np.linalg.norm(A,np.inf))
print(np.max(np.sum(np.abs(A),axis=1)))



