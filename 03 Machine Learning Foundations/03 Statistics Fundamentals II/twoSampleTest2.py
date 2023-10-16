from scipy.stats import ttest_ind
#import codecademylib3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# store the data
veryants = pd.read_csv('veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run t-tests
tstat1, a_b_pval = ttest_ind(a, b)
tstat2, a_c_pval = ttest_ind(a, c)
tstat3, b_c_pval = ttest_ind(b, c)

print(a_b_pval, a_c_pval, b_c_pval)
# determine significance. Are pValues <0.05?
a_b_significant = True
a_c_significant = True
b_c_significant = False

# create plot
sns.boxplot(data=veryants, x='Store', y='Sale')
plt.show()