'''
Plot a histogram of the residuals to check the normality assumption. Is this assumption met?
'''
# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()

# Calculate fitted values
fitted_values = results.predict(students)

# Calculate residuals
residuals = students.score - fitted_values

# Plot a histogram of the residuals here:
plt.hist(residuals)

plt.show()
plt.clf()

'''
Now, check the homoscedasticity assumption by plotting the residuals 
against the fitted values (fitted_values on the x-axis and residuals on the y-axis). Is this assumption met?
'''

# Plot the residuals against the fitted vals here:
plt.scatter(fitted_values, residuals)
plt.show()