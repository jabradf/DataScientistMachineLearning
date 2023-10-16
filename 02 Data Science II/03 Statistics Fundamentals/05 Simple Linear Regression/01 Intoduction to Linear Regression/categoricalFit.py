'''
Create and fit a regression model of score predicted by breakfast 
using sm.OLS.from_formula() and print out the coefficients.
'''

'''
Code has been provided for you in script.py to calculate the mean 
test score for students who ate breakfast (saved as mean_score_breakfast) 
and the mean score for students who did not eat breakfast (saved as 
mean_score_no_breakfast). Calculate and print the difference in mean scores. 
Can you find how this number relates to the regression output?
'''
# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('test_data.csv')

# Calculate and print group means
mean_score_no_breakfast = np.mean(students.score[students.breakfast == 0])
mean_score_breakfast = np.mean(students.score[students.breakfast == 1])
print('Mean score (no breakfast): ', mean_score_no_breakfast)
print('Mean score (breakfast): ', mean_score_breakfast)

# Fit the model and print the coefficients
model = sm.OLS.from_formula('score ~ breakfast', students)
results = model.fit()
print(results.params)

# Calculate and print the difference in group means
diff = mean_score_breakfast - mean_score_no_breakfast
print(diff)