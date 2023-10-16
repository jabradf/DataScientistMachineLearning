# import libraries
#import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# load data
heart = pd.read_csv('heart_disease.csv')

print(heart.head())

#Do you think there is a relationship between these variables?
sns.boxplot(data=heart, y=heart.thalach, x=heart.heart_disease)
plt.show()

thalach_no_hd = heart.thalach[heart.heart_disease=='absence']
thalach_hd = heart.thalach[heart.heart_disease=='presence']
#print(thalach_hd)
meanDiff = np.mean(thalach_no_hd) - np.mean(thalach_hd)
print("mean diff hd:", meanDiff)
print("median diff:", np.median(thalach_no_hd) - np.median(thalach_hd))

#############
# Run tests
from scipy.stats import ttest_ind
tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print('p-value two-sample t-test: ', pval)
# <0.05, significantly different

#############
# Exploration
# first box plot:
sns.boxplot(x=heart.heart_disease, y=heart.trestbps)
plt.title("resting bps")
plt.show()

trestbps_no_hd = heart.trestbps[heart.heart_disease=='absence']
trestbps_hd = heart.trestbps[heart.heart_disease=='presence']
meanDiff = np.mean(trestbps_no_hd) - np.mean(trestbps_hd)
print("Resting BPS mean diff hd:", meanDiff)
print("median diff:", np.median(trestbps_no_hd) - np.median(trestbps_hd))
tstat, pval = ttest_ind(trestbps_hd, trestbps_no_hd)
print('p-value two-sample t-test: ', pval)
print(" ")


################## 
# second box plot:
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.title("age")
plt.show()

age_no_hd = heart.age[heart.heart_disease=='absence']
age_hd = heart.age[heart.heart_disease=='presence']
meanDiff = np.mean(age_no_hd) - np.mean(age_hd)
print("Age BPS mean diff hd:", meanDiff)
print("median diff:", np.median(age_no_hd) - np.median(age_hd))
tstat, pval = ttest_ind(age_hd, age_no_hd)
print('p-value two-sample t-test: ', pval)
print(" ")

# third box plot:
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.chol)
plt.title("Cholesterol")
plt.show()

chol_no_hd = heart.chol[heart.heart_disease=='absence']
chol_hd = heart.chol[heart.heart_disease=='presence']
meanDiff = np.mean(chol_no_hd) - np.mean(age_hd)
print("Cholesterol BPS mean diff hd:", meanDiff)
print("median diff:", np.median(chol_no_hd) - np.median(chol_hd))
tstat, pval = ttest_ind(chol_hd, chol_no_hd)
print('p-value two-sample t-test: ', pval)      # above the threshold, no significance
print(" ")

###############
# box plot chest pain types
plt.clf()
sns.boxplot(x=heart.cp, y=heart.thalach)
plt.title("Chest pain vs heart rate")
plt.show()

# Chest pain types:
#print(heart['cp'].unique())
thalach_typical = heart.thalach[heart.cp=='typical angina']
thalach_asymptom = heart.thalach[heart.cp=='asymptomatic']
thalach_nonangin = heart.thalach[heart.cp=='non-anginal pain']
thalach_atypical = heart.thalach[heart.cp=='atypical angina']

# comparing four types here; use ANOVA test!
from scipy.stats import f_oneway
Fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print('ANOVA p value: ', pval)

# find which of the pairs have this low value using tukey test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(heart.thalach, heart.cp, 0.05)
print(tukey)

# get a contingency table for relationship between chest pain type and heart disease presence
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

# Run a chi^2 test on the table
from scipy.stats import chi2_contingency
chi2, pval, dof, exp = chi2_contingency(Xtab)
print("contingency table pvalue:", pval)
# very low p value so there is a significant association


######
# compare men vs women
plt.clf()
sns.boxplot(x=heart.sex, y=heart.thalach)
plt.title("Heart rate vs Sex")
plt.show()
'''
hol_no_hd = heart.chol[heart.heart_disease=='absence']
chol_hd = heart.chol[heart.heart_disease=='presence']
meanDiff = np.mean(chol_no_hd) - np.mean(age_hd)
print("Cholesterol BPS mean diff hd:", meanDiff)
print("median diff:", np.median(chol_no_hd) - np.median(chol_hd))
tstat, pval = ttest_ind(chol_hd, chol_no_hd)
print('p-value two-sample t-test: ', pval)      # above the threshold, no significance
print(" ")'''