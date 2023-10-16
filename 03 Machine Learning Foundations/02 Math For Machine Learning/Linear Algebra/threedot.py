import numpy as np


a = np.array([[2,3,4], [-2,-2,-2], [0,1,0], [-1,-3,-2]])
b = np.array([[-1,-2,-1], [2,1,-2], [3,0,-3]])
c = np.array([1,2,3])

d = np.dot(a,b)
e = np.dot(d,c)

print(d.shape)