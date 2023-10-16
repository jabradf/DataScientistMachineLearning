'''
In script.py, you’ll see the code (from the previous exercise) to fit a 
model that predicts test score using hours_studied. Print the coefficients of this model using .params.
'''

'''
Using your model, what is the predicted score for a student who spent 3 hours 
studying? Save the result as pred_3hr and print it out. Calculate your answer 
by plugging into the formula for a line (instead of using .predict()).
'''

'''
What is the predicted score for a student who spent 5 hours studying? Use the .predict() 
method to calculate your answer and save it as pred_5hr, then print it out.
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

# Print the model params
print(results.params)

# Calculate and print `pred_3hr` here:
pred_3hr = results.params[1] * 3 + results.params[0]
print(pred_3hr)
# Calculate and print `pred_5hr` here:
newdata = {"hours_studied":[5]}
pred_5hr = results.predict(newdata)
print(pred_5hr)