# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())
# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed, codecademy.score)
# Show then clear plot
plt.title("Score vs Completed")
plt.show() # Show the plot
plt.clf() # Clear the plot

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', codecademy)
results = model.fit()
print(results.params)

# Intercept interpretation:
# If zero is completed, it is expected that the score is 13.21.

# Slope interpretation:
# For every increase in completed by 1, score increases by 1.3

# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)
plt.plot(codecademy.completed, results.predict(codecademy))
plt.title("Score vs Completed with regression")
# Show then clear plot
plt.show() # Show the plot
plt.clf() # Clear the plot

# Predict score for learner who has completed 20 prior lessons
pred20 = {'completed':[20]}
print(results.predict(pred20))

# Calculate fitted values
fitted_values = results.predict(codecademy)

# Calculate residuals
residuals = codecademy.score - fitted_values
# Check normality assumption
plt.hist(residuals)
# Show then clear the plot
plt.title("Residuals")
plt.show() # Show the plot
plt.clf() # Clear the plot

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
# Show then clear the plot
plt.title("Homoscedasticity Assumption")
plt.show() # Show the plot
plt.clf() # Clear the plot

# Create a boxplot of score vs lesson
sns.boxplot(x='lesson', y='score', data=codecademy)
# Show then clear plot
plt.title("Score vs Lesson")
plt.show() # Show the plot
plt.clf() # Clear the plot

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', codecademy)
results = model.fit()
print(results.params)

# Calculate and print the group means and mean difference (for comparison)
groupmeans = codecademy.groupby('lesson').mean().score
print(groupmeans)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()