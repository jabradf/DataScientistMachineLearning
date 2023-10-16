import numpy as np

# Taking a 3 * 3 matrix
A = np.array([[2, 4, -2],
              [-2, 0, 1],
              [3, -3, 0]])
 
# Calculating the inverse of the matrix
print(np.linalg.inv(A))