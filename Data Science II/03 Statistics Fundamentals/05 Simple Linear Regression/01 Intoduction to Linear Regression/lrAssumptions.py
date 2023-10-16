'''
Fit a model on the students dataset that predicts test score using 
hours_studied as a predictor. Calculate the fitted values for this 
model and save them as fitted_values.
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

# Calculate `fitted_values` here:
fitted_values = results.predict(students.hours_studied)
print(fitted_values.head())


'''
Calculate the residuals for this model and save the result as residuals.
'''
# Calculate `residuals` here:
residuals = students.score - fitted_values


'''
Print out the first 5 values in residuals and inspect them. Can you 
make sense of these numbers? What is the difference between a positive and negative residual?
'''
# Print the first 5 residuals here:
print(residuals.head())