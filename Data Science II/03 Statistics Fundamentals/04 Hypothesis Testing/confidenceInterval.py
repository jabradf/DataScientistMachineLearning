'''
The code to generate null_outcomes has been provided for you. 
Calculate an interval covering the middle 90% of the values in 
null_outcomes. Save the output in a variable named null_90CI and 
print it out. Is the observed value of 41 purchases inside or outside 
this interval?
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the 90% interval here:
null_90CI = np.percentile(null_outcomes, [5, 95])