import numpy as np

#Find P when given PA = B
A = np.array([[1,4,7,-2],
              [3,0,-2,-1],
              [-4,2,1,0],
              [-8,-3,-1,2]])

B = np.array([[-4,2,1,0],
              [3,0,-2,-1],
              [-8,-3,-1,2],
              [1,4,7,-2]])

# Solve using the transposed forms, since you cannot divide matrices!
P = np.linalg.solve(A.T, B.T).T > 0.5   # add the threshold for true/false output
print(P)