import pandas as pd
import matplotlib.pyplot as plt 

housing = pd.read_csv('housing_sample.csv')

print(housing.head())

#create your scatter plot here:
plt.scatter(x = housing.beds, y = housing.sqfeet)
plt.xlabel('Beds')
plt.ylabel('Area (Square Feet)')

plt.show()


######
# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.beds, housing.sqfeet)
print(cov_mat_sqfeet_beds)