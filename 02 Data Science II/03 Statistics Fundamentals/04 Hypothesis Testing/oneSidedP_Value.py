'''
The code you wrote to generate null_outcomes is available here. 
Use null_outcomes to estimate the p-value for a binomial hypothesis 
test with the following null and alternative hypotheses:

Null: the probability of a purchase was 10%
Alternative: the probability of a purchase rate was LESS THAN 10%
In other words, calculate the proportion of values in null_outcomes 
that are less than or equal to 41 (the observed number of purchases 
that we calculated earlier). Save this number as a variable named p_value 
and print it out.

Try pressing “Run” a few times; You should see slightly different values 
of p_value each time. What do you think the true probability is?
'''

import numpy as np
import pandas as pd

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41)/len(null_outcomes) 
print(p_value)