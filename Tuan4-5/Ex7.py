# 3x+3.2y=118.4
# 3.5x+3.6y=135.2
import numpy as np
A=np.array([[3,3.2],[3.5,3.6]])
b=np.array([118.4,135.2])
print(np.linalg.solve(A,b.T))