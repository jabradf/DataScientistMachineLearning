import numpy as np
import pandas as pd
#import codecademylib3
import matplotlib.pyplot as plt

eigenvalues = pd.read_csv('eigenvalues.csv')['eigenvalues'].values

# 1. Find the proportion of information for each eigenvector, which is equal to the eigenvalues divided by the sum of all eigenvalues
info_prop = eigenvalues / eigenvalues.sum()
print(info_prop)

## Plot the principal axes vs the information proportions for each principal axis
plt.plot(np.arange(1,len(info_prop)+1),info_prop, 'bo-', linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principal Axes')
plt.xticks(np.arange(1,len(info_prop)+1))
plt.ylabel('Percent of Information Explained')
plt.show()
plt.clf()

'''
From this plot, we see that the first principal component explains about 50% of the 
variation in the data, the second explains about 30%, and so on.

Another way to view this is to see how many principal axes it takes to reach around 95% 
of the total amount of information. Ideally, we’d like to retain as few features as possible 
while still reaching this threshold.

To do this, we need to calculate the cumulative sum of the info_prop vector we created earlier:
'''
# 2. Find the cumulative sum of the proportions
cum_info_prop = np.cumsum(info_prop)

## Plot the cumulative proportions array
plt.plot(cum_info_prop, 'bo-', linewidth=2)
plt.hlines(y=.95, xmin=0, xmax=15)
plt.vlines(x=3, ymin=0, ymax=1)
plt.title('Cumulative Information percentages')
plt.xlabel('Principal Axes')
plt.xticks(np.arange(1,len(info_prop)+1))
plt.ylabel('Cumulative Proportion of Variance Explained')
plt.show()

# From this plot, we see that four principal axes account for 95% of the variation in the data.
