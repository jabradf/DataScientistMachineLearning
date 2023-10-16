'''
Using the dataset students (which has been loaded for you in script.py), 
plot a scatter plot of score (y-axis) against breakfast (x-axis) to see scores 
for students who did and did not eat breakfast.


Code has been provided for you in script.py to calculate the mean test 
score for students who ate breakfast and the mean score for students who 
did not eat breakfast. Use these numbers to plot the best-fit line on top of the scatter plot.
'''

# Load libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv('test_data.csv')

# Calculate group means
grouped = students.groupby('breakfast').mean().score
print(grouped)

# Create the scatter plot here:
plt.scatter(students.breakfast, students.score)

# Add the additional line here:
plt.plot([0,1], [grouped[0], grouped[1]])

# Show the plot
plt.show()