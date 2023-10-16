# program to compute magnitude of a vector
 
# importing required libraries
import numpy
import math
 
# function definition to compute magnitude o f the vector
def magnitude(vector):
    return math.sqrt(sum(pow(element, 2) for element in vector))
 
# displaying the original vector
v = numpy.array([-2, -3, 0, 5, 1])
print('Vector:', v)
 
# computing and displaying the magnitude of the vector
mag = magnitude(v)
print('Magnitude of the Vector:', mag)
print("sqrt of: ", mag**2)