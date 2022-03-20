import numpy as np
T = np.array([[0.6, 0.7], [0.4, 0.3]])
p = np.array([[0.5], [0.5]])
k = int(input())
for i in range(k):
  T = np.dot(T,T)
print(np.dot(T,p))
# 100 so da qua lon (check)