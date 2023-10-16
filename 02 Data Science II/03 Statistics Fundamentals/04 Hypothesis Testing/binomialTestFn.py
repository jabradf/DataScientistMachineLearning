'''
The simulation_binomial_test() function has been outlined 
for you in script.py. Add the following parameters to the function (in this order):

observed_successes (the observed sample statistic, eg., 41 purchases)
n (the sample size, eg., 500 visitors)
p (the null probability of success, eg., 0.10)
'''

'''
Next, edit the simulation_binomial_test() function to remove all of the hard-coded 
values (eg., 500, 0.1, 0.9, and 41) so that the proper parameters are used in each calculation.


Uncomment the code at the bottom of script.py to test out your function and compare 
the results to the SciPy binom_test() function. Do you get similar answers?
'''

import numpy as np
import pandas as pd
from scipy.stats import binom_test

def simulation_binomial_test(observed_successes, n, p):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  #calculate a 1-sided p-value
  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  
  #return the p-value
  return p_value

#Test your function below by uncommenting the code below. You should see that your simulation function gives you a very similar answer to the binom_test function from scipy:

p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)
