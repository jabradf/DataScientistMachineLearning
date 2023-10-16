import scipy.stats as stats

# value of interest
# change this
x = 3

# sample size
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)

## Question 2
x=7
n=20
prob_2 = stats.binom.pmf(x, n, 0.5)
print(prob_2)
