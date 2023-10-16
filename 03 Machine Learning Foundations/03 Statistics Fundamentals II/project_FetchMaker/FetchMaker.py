# Import libraries
import numpy as np
import pandas as pd
import os
#import codecademylib3

# Import data
path = 'dog_data.csv'
check_file = os.path.isfile(path)
if check_file:
    dogs = pd.read_csv('dog_data.csv')
else: 
    dogs = pd.read_csv('project_FetchMaker\dog_data.csv')


whippet_rescue = dogs.is_rescue[dogs.breed=='whippet']
#print(whippet_rescue)

num_whippet_rescues = np.sum(whippet_rescue==1)
print("number of whippet rescues: ", num_whippet_rescues)
num_whippets = len(whippet_rescue)
print("number of whippets: ", num_whippets)

# Estimates are 8% are rescues
# Compare a sample statistic (8%) with a categorical value (is rescued): Run a binoial test
from scipy import stats
pvalBinom = stats.binom_test(n=num_whippets, x=num_whippet_rescues, p=0.08)  # don't use greate as it specifies "more or less"
print("p value of recues: ", pvalBinom)
# p value is over 0.05 so it's not significant.

##############
# Mid sized dog weights
wt_whippets = dogs.weight[dogs.breed=='whippet']
wt_terriers = dogs.weight[dogs.breed=='terrier']
wt_pitbulls = dogs.weight[dogs.breed=='pitbull']

# run a test for all three breeds (categorical) and association of weights (quantitive). Use ANOVA test!
from scipy.stats import f_oneway
fstat, pvalAnova = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print("pVal for ANOVA: ", pvalAnova)
# pVal is basically zero so there is at least one pair that is significant. Find out which by using tukey test.
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]
tukey_results = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed, 0.05)
print("tukey results: ", tukey_results)
# the pairs with statistically diff weights are pitbull/terrier and terrier/whipper


############### 
# Poodle and shitzu colours
# Subset to just poodles and shihtzus
print("#################")
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]
#print(dogs_ps.columns)
Xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
print(Xtab)
# compare categorical (breed) and categorical (colour): chi squared test
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(Xtab)
print("pvalue of breed vs colour: ", pval)
# significance of 0.0053 which is below 0.05; statistical significance between breed and colour type!
