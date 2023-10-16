'''
Use the random.choice() function from NumPy to simulate a single visitor 
to Live-it-LIVE.com, who has a 10% chance of making a purchase (p=0.1). 
Save the outcome as a variable named one_visitor and print it. If the visitor 
made a purchase, the value of one_visitor should be ['y']; if they did not make 
a purchase, it should be ['n'] (just like in the original data!).

Did that one simulated visitor make a purchase? Try pressing “Run” a few more t
imes and see if you ever observe a different outcome. 
'''

import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')
print(monthly_report.head(10))
#simulate one visitor:
one_visitor = np.random.choice(['y', 'n'] , size=1, p=[0.9, 0.1])
print(one_visitor)


'''
Now, create a new list named simulated_monthly_visitors, which contains the 
randomly-generated outcomes for 500 visitors to Live-it-LIVE.com (still with a 
10% chance of a purchase). Print simulated_monthly_visitors out. Do you see any 
visitors in this list who made a purchase?
'''

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'] , size=500, p=[0.9, 0.1])
print(simulated_monthly_visitors)