# import libraries
import pandas as pd
import numpy as np

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']
print(yes_hd.head(10))

chol_hd = yes_hd.chol
#print(chol_hd.head())
chol_mean = np.mean(chol_hd)
print("yes hd chol: ", chol_mean)  # higher than 240?

from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2) # threshold is 0.05 = significant!


# repeat for no_hd
chol_hd = no_hd.chol
#print(chol_hd.head())
chol_mean = np.mean(chol_hd)
print("no hd chol: ", chol_mean)  # higher than 240?

from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2) # threshold is 0.05 = not significant

num_patients = len(heart)
print("number of patients: ", num_patients)
num_highfbs_patients = np.sum(heart.fbs == 1)
print("num high fbs: ", num_highfbs_patients)
expected = num_patients * 0.08
print("expected: ", expected)

from scipy.stats import binom_test
result = binom_test(x= num_highfbs_patients, n=num_patients, p=0.08, alternative='greater')
print("null: ", result)