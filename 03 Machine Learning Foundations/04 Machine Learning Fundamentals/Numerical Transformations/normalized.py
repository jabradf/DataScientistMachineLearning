import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')

## add code below
## get spent feature
spent = coffee.spent

#find the max spent
max_spent = np.max(spent)

#find the min spent
min_spent = np.min(spent)

#find the difference
spent_range = max_spent-min_spent
print(spent_range)

#normalize your spent feature
spent_normalized = (spent - min_spent) / (max_spent - min_spent)

#print your results
print(spent_normalized)