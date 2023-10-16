'''
In script.py, a variable called rand_vars_7 contains 5000 random 
draws from the Poisson distribution with lambda = 7.

Calculate and print the variance of rand_vars_7.


Calculate and print the minimum value and maximum value of rand_vars_7.


In script.py, a variable called rand_vars_17 contains 5000 random draws from the Poisson distribution with lambda = 17.

Calculate and print the variance of rand_vars_17.


Calculate and print the minimum and maximum values of rand_vars_17.

Note that the range of values of rand_vars_17 is wider than rand_vars_7.
'''


import scipy.stats as stats
import numpy as np

## For checkpoints 1 and 2
# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)

## Checkpoint 1
# print variance of rand_vars_7
print(np.var(rand_vars_7))

## Checkpoint 2
# print minimum and maximum of rand_vars_7
print(min(rand_vars_7), max(rand_vars_7))

## For checkpoints 3 and 4
# 5000 draws, lambda = 17
rand_vars_17 = stats.poisson.rvs(17, size = 5000)

## Checkpoint 3
# print variance of rand_vars_17
print(np.var(rand_vars_17))

## Checkpoint 4
# print minimum and maximum of rand_vars_17
print(min(rand_vars_17), max(rand_vars_17))
