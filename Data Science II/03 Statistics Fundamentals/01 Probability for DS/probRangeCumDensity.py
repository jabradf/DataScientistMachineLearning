'''
Working at a call center where the average number of calls between 9am and 10am is 15 calls, 
what is the probability of observing more than 20 calls?

Uncomment prob_more_than_20 and assign this probability to the variable. Then print prob_more_than_20.'''
import scipy.stats as stats

## Checkpoint 1
# calculate prob_more_than_20
prob_more_than_20 = 1-stats.poisson.cdf(20, 15)

print(prob_more_than_20)

## Checkpoint 
# calculate prob_17_to_21
prob_17_to_21 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)

print(prob_17_to_21)
