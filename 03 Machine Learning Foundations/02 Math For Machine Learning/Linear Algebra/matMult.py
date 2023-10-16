import numpy as np

#Find P when given PA = B
A = np.array([[2,-3,1],
              [-2,-1,4],
              [0,2,2]])

B = np.array([[3,-2,1],
              [1,-1,2],
              [-2,2,0]])


c = np.matmul(A,B)
print(c)