'''
Use ttest_1samp() to run the hypothesis test described above (null: the 
average price is 1000 Rupees; alternative: the average price is not 1000 Rupees).

Store the p-value in a variable called pval. Remember that it is the second 
output of the ttest_1samp() function. We won’t use the first output, the t-statistic, 
so you can store it in a variable with whatever name you’d like.
'''

from scipy.stats import ttest_1samp
import numpy as np

prices = np.genfromtxt("prices.csv")
print(prices)

prices_mean = np.mean(prices)
print("mean of prices: " + str(prices_mean))

# use ttest_1samp to calculate pval
tstat, pval = ttest_1samp(prices, 1000)


'''
Print out pval to the console.

Does the p-value you got make sense, knowing the mean of prices and having inspected 
the data? (Look at the hint for an answer to this question).
'''

# print pval
print(pval)