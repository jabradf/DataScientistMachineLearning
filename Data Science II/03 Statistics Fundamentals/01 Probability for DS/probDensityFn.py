'''Following the same Normal(167.64, 8) distribution, assign the variable prob the 
probability that a randomly chosen woman is less than 175 cm tall. You should use the 
stats.norm.cdf() method.import scipy.stats as stats
'''
import scipy.stats as stats

prob = stats.norm.cdf(175, 167.64, 8)
print(prob)