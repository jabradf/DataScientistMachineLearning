from numpy import arccos, array
from numpy.linalg import norm
import math

#function for calculating the angle using numpy
def angles(u, v): 
  #using the arccos function from numpy
  return arccos(u.dot(v)/(norm(u)*norm(v)))


#defining the vectors
u = array([3, -1, 2])
v = array([0, -1, 1])

#function call to compute the angle
c= angles(u,v)

# The function returns the angle in radians, so convert to degrees
angle= math.degrees(c)

print("the vectors are=",u,"and",v)
print("the angle between the two vectors is=",angle)