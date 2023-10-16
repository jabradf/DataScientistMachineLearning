'''
you’ll see the code we used in the previous exercise to generate simulated_monthly_visitors, 
a list of 500 simulated outcomes, 'y' (with probability 0.1) or 'n', indicating whether each 
imaginary site visitor made a purchase.

Add a line of code to calculate the number of those simulated visitors who made a purchase. 
Save the result as num_purchased and print it out.
'''

'''
Inspect the value of num_purchased from the previous instruction. Is it close to 50 
(which is what we would expect for a purchase probability of 10%)? Less than? Greater 
than? Now run it a few more times and see what other values of num_purchased 
you observe. What’s the farthest number from 50 that you observe after pressing “Run” 5 times?
'''
import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
#print(simulated_monthly_visitors)
#calculate the number of simulated visitors who made a purchase:
num_purchased  = np.sum(simulated_monthly_visitors == 'y')
print(num_purchased)