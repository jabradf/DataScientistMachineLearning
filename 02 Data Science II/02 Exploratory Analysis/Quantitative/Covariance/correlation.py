import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import pearsonr

housing = pd.read_csv('housing_sample.csv')

# calculate corr_sqfeet_beds and print it out:
corr_sqfeet_beds, p = pearsonr(housing.beds, housing.sqfeet)

print(corr_sqfeet_beds)
# create the scatter plot here:
plt.xlabel('Number of beds')
plt.ylabel('Number of sqfeet')
plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.show()
