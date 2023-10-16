import scipy.stats as stats

'''
assign the variable prob_1 to the probability of observing 3 or fewer heads from 10 
fair coin flips using the cumulative distribution function. Then print prob_1.

Use the binom.cdf() method from the scipy.stats library.
'''
## Checkpoint 1
prob_1 = stats.binom.cdf(3, 10, 0.5)
print(prob_1)

# compare to pmf code
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5)\
       + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))


## Checkpoint 2
prob_2 = 1 - stats.binom.cdf(5, 10, 0.5)
print(prob_2)


## Checkpoint 3
prob_3 = stats.binom.cdf(5, 10, 0.5) - stats.binom.cdf(1, 10, 0.5)
print(prob_3)

# compare to pmf code
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5)\
       + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))