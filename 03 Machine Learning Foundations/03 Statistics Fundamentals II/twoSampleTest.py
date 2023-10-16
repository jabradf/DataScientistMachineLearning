import pandas as pd
import matplotlib.pyplot as plt
#import codecademylib3
from scipy.stats import ttest_ind
data = pd.read_csv('version_time.csv')

#separate out times for  two versions
old = data.time_minutes[data.version=='old']
new = data.time_minutes[data.version=='new']

#run the t-test here:
tstat, pval = ttest_ind(old, new)
print(pval)

'''
Using a significance threshold of 0.05, is there a significant difference between the average amount of time visitors are spending on the old and new versions of the website? In script.py set the value of significant equal to True if there is a significant difference and False if not.
'''
#determine significance
significant = True  # less than 0.05, so it's significant

#plot overlapping histograms
plt.hist(old, alpha=.8, label='old')
plt.hist(new, alpha=.8, label='new')
plt.legend()
plt.show()