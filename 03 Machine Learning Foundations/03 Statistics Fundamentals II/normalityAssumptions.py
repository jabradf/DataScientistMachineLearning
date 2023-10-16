'''
The standard deviations of the groups should be equal.
To check this assumption, it is normally sufficient to divide one standard deviation by the other and see if the ratio is “close” to 1. Generally, a ratio between 0.9 and 1.1 should suffice.
'''

#import codecademylib3
import numpy as np
import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("1.csv")
dist_2 = np.genfromtxt("2.csv")

#calculate ratio of standard deviations:
ratio = np.std(dist_1) / np.std(dist_2)
print(ratio)  # not between threshold of 0.9-1.1

#check normality assumption; do they have a distribution hump?
normal_assumption = True

#plot histograms of each distribution
plt.hist(dist_1, alpha = .8, normed = True, label = 'dist 1')
plt.hist(dist_2, alpha = .8, normed = True, label = 'dist 2')
plt.legend()
plt.show()