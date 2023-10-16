import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
#import codecademylib3_seaborn 

coffee = pd.read_csv('starbucks_customers.csv')
#print(coffee.info())
ages = coffee.age
min_age = np.min(ages)
print("min age is: ", min_age)
max_age = np.max(ages)
print("max age is:", max_age)
age_spread = max_age - min_age
print("age spread is:", age_spread)
mean_age = np.mean(ages)
print("mean of ages is: ", mean_age)
centered_ages = ages - mean_age
print(centered_ages)

plt.hist(centered_ages) #, bins = 5, color = 'g')
 
#label our visual
plt.title('Starbucks Distance Data Centered')
plt.xlabel('Distance from Mean')
plt.ylabel('Count')
plt.show();