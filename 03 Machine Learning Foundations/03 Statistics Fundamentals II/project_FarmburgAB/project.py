# Import libraries
#import codecademylib3
import pandas as pd
import numpy as np
import os

# Read in the `clicks.csv` file as `abdata`
path = 'clicks.csv'
check_file = os.path.isfile(path)
if check_file:
    abdata = pd.read_csv('clicks.csv')
else: 
    abdata = pd.read_csv('project_FarmburgAB\clicks.csv')

print(abdata.head())
# run a chi squared test
from scipy.stats import chi2_contingency
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab) # group A has the highest number of purchases
chi2, pval, dof, expected = chi2_contingency(Xtab)
print("pval between group and purchased: ", pval)
# p is near zero so it's under the 0.05 threshold; there is a significant difference between purchase rates

#############
#get total visitors
num_visitors = len(abdata)
print("num visitors: ", num_visitors)
num_sales_needed_099 = (1000/0.99)
print("number of sales needed at 99c:", num_sales_needed_099)
p_sales_needed_099 = num_sales_needed_099 / num_visitors
print("p sales needed:", p_sales_needed_099)

num_sales_needed_199 = (1000/1.99)
print("number of sales needed at $1.99:", num_sales_needed_199)
p_sales_needed_199 = num_sales_needed_199 / num_visitors
print("p sales needed:", p_sales_needed_199)

num_sales_needed_499 = (1000/4.99)
print("number of sales needed at $4.99:", num_sales_needed_499)
p_sales_needed_499 = num_sales_needed_499 / num_visitors
print("p sales needed:", p_sales_needed_499)

print('##################')
# Get sample sizes and purchases for each group
#Group A
groupA = abdata.is_purchase[abdata.group=='A']
samp_size_099 = len(groupA)
sales_099 = np.count_nonzero(groupA == 'Yes')
#print(samp_size_099, sales_099)

# Group B
groupB = abdata.is_purchase[abdata.group=='B']
samp_size_199 = len(groupB)
sales_199 = np.count_nonzero(groupB == 'Yes')
#print(samp_size_199, sales_199)

# Group C
groupC = abdata.is_purchase[abdata.group=='C']
samp_size_499 = len(groupC)
sales_499 = np.count_nonzero(groupC == 'Yes')
#print(samp_size_499, sales_499)

from scipy.stats import binom_test
pvalueA = binom_test(x=sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')
print("pvalue group A: ",pvalueA)

pvalueB = binom_test(x=sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')
print("pvalue group B: ",pvalueB)

pvalueC = binom_test(x=sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')
print("pvalue group C: ",pvalueC)

# what is the statistical significant value to choose, based on 0.05 threshold?
# Group C is the only one below this, at 0.0279 so group C is the answer: charge $4.99