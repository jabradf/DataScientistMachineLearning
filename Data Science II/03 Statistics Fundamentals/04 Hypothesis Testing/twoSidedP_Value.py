'''
The code you wrote to generate null_outcomes is available here. 
Use null_outcomes to calculate the p-value for a two-sided test 
(alternative hypothesis is that the purchase probability was DIFFERENT 
FROM 10%). Remember that, if the purchase rate is 10%, we expect 50 of 
the 500 visitors to make a purchase.

In other words, calculate the proportion of values in null_outcomes that 
are less than or equal to 41 (the number of purchases we observed in our 
sample, which is 9 fewer than 50) OR greater than or equal to 59 (which 
is 9 purchases more than 50). Save this number as a variable named 
p_value and print it out.

Again, try pressing run a few times to observe a few different estimates 
of p_value. What do you think the true p-value is for this test?
'''

import numpy as np
import pandas as pd

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:
outcomes = np.array(null_outcomes)
p_value = np.sum((outcomes <= 41) | (outcomes >= 59))/len(outcomes)
print(p_value) #output: 0.12
