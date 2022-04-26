import numpy as np
import matplotlib.pyplot as plt
## y = wo + w1x => (1)wo + (1400)w1
X = np.array([[1, 1400], [1, 1600],
[1,1700],[1, 1875],
[1, 1100],[1, 1550],
[1,2350], [1,2450],
[1,1425],[1,1700]])
b = np.array([245, 312, 279, 308, 199,219, 405, 324, 319, 255])
## w = inv(A.T@A)@A.T@b.T
w = np.linalg.inv(X. T@X)@X. T@b.T
print(w)
x_space = 2000
y_price = w[0] + w[1]*x_space
y_pred = w[0] + w[1]*X[:,1]
print(y_price)
fig = plt.figure()
plt.plot(X[:,1], b, 'ro')
plt.plot(X[:,1], y_pred, 'b')
plt.plot(X[:,1], y_pred, 'go')
plt.show()