import numpy as np

# Given
# 2 x 3 matrix
A = np.array([[2,3,-4], [-2, 1, -3]])
# 2 x 3 matrix
B = np.array([[1,-1,4], [3,-3,3]])
# 3 x 2 matrix
C = np.array([[1, 2], [3, 4], [5, 6]])

# Calculate D = 4A - 2B
D = 4*A - 2*B
print(D)

# Calculate E = AC
E = np.matmul(A,C)
print(E)

# Calculate F = CA
F = np.matmul(C,A)
print(F)

#############################################

# Given
A = np.array([[1,-1,1], [0,1,0], [-1,2,1]])
B = np.array([[0.5,1.5,-0.5], [0,1,0], [0.5,-0.5,0.5]])

'''identity = np.eye(4)
zero_vector = np.zeros((5))
zero_matrix = np.zeros((3,2))
A_transpose = A.T'''

'''
Two NumPy arrays are given, A and B, representing two 3x3 matrices. Print out the matrix product of AB and the matrix product of BA.

What does this say about the relationship between matrix A and matrix B?
'''
AB = np.matmul(A,B)
print(AB)
BA = np.matmul(B,A)
print(BA)

'''
Print out the transpose of both matrix A and matrix B. What is the first row of each transposed matrix?
'''
print(A.T)
print(B.T)


################
# dot solving
a = np.array([1,7,3])
b = np.array([-2,4,1])
c = np.dot(a,b)

print(c)