import pandas as pd

npi = pd.read_csv("npi_sample.csv")

#Frequencies
special_authority_freq = pd.crosstab(npi.special, npi.authority)
print(special_authority_freq)

#####
#Proportions
# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq / len(npi)

# print out special_authority_prop
print(special_authority_prop)


#######
#Marginal Proportions

# calculate and print authority_marginals
authority_marginals =  special_authority_prop.sum(axis=0)
print(authority_marginals)

# calculate and print special_marginals
special_marginals =  special_authority_prop.sum(axis=1)
print(special_marginals)


#####
# Expected Contingency Table
from scipy.stats import chi2_contingency
import numpy as np

print()
# calculate the expected contingency table if there's no association and save it as expected
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)

# print out the expected frequency table
print("expected contingency table (no association):")
print(np.round(expected))



#####
# Chi Squared Statistic
print()
# calculate the chi squared statistic and save it as chi2, then print it:
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)
print(chi2)