# Import libraries
import pandas as pd
import numpy as np

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

print(lifespans.head())

vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']
#print(len(vein_pack_lifespans))
average = np.mean(vein_pack_lifespans)
print("the average lifespan for vein pack is: ", average)

from scipy.stats import ttest_1samp
av_lifespan = 73

#compare the sample stat to a population quantative value: one sample T test!
t_statistic, p_value = ttest_1samp(vein_pack_lifespans, av_lifespan)
print("P value is : ", p_value)
# 5.97e-07 is much smaller than 0.05 so it is statistically significant.

##############
# Get data for artery pack
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']
#print(len(artery_pack_lifespans))
average2 = np.mean(artery_pack_lifespans)
print("the average lifespan for artery pack is: ", average2)

# run a 2 sample T test:
from scipy.stats import ttest_ind
t_stat2, p_val2 = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print("P value is : ", p_val2)
#P value is slightly above the threshold of 0.05 so it is not statistically significant.


#########################
# Side Effects
print("#################")
print(iron.head())
contingency = pd.crosstab(iron.pack, iron.iron)
print(contingency)

# run a chi square test
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(contingency)
print("p value of crosstab: ", pval)
# pval is very small, so there is an association between the chosen pack and the iron levels!
