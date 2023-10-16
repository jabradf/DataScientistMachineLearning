import numpy as np
# Represent the following system in NumPy matrix/vector form, then solve for x, y, and z

# Given
'''
2x -3y + z = 2
3x + y + z = -1
-x - 2y - z = 4
'''
# create the matrix, remembering the order of x,y,z
A = np.array([[2, -3, 1], 
              [3, 1, 1], 
              [-1, -2, -1]])

# create the b form
b = b = np.array([2,-1,1])

# solve for x, y, and z
x,y,z = np.linalg.solve(A,b)

# print as a matrix
print((x,y,z))

##############
#second example
'''
x -3y +z = 4
2x -8y +8z = -2
-6x +3y -15z = 9

'''
A = np.array([[1, -3, 1], 
              [2, -8, 8], 
              [-6, 3, -15]])

# create the b form
b = b = np.array([4,-2,9])

# solve for x, y, and z
x,y,z = np.linalg.solve(A,b)

# print as a matrix
print((x,y,z))