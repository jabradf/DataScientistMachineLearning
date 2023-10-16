import pandas as pd
from scipy.stats import chi2_contingency

# read in and print data
ants = pd.read_csv("ants_grade.csv")
print(ants.head())

# create contingency table
table = pd.crosstab(ants.Grade, ants.Ant)
print(table)

# run Chi-Square test and print p-value
chi2, pval, dof, expected = chi2_contingency(table)
print(pval)

# determine significance (P <0.05?)
significant = False