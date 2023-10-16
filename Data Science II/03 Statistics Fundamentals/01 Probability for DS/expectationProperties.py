import scipy.stats as stats
import numpy as np

'''
At the end of the year, your company’s boss decides that the 
end-of-year bonus will be 8% of each employee’s salary. If the 
average salary in the company is $75,000, what is the expected value 
(or average value) of the bonuses?
'''


## Checkpoint 1
expected_bonus = 75000 * 0.08
print(expected_bonus)


'''
Let’s say that the number of goals a soccer team scores follows the Poisson 
distribution with lambda equal to four. Uncomment num_goals and set it equal 
to 100 random draws from games following this Poisson distribution.

You can do this using the stats.poisson.rvs() method from the scipy library 
with lambda equal to four and 100 random draws. Click the hint if you need more guidance.
'''
## Checkpoint 2
num_goals = stats.poisson.rvs(4, size=100)
print(num_goals)

## Checkpoint 3
print(np.var(num_goals))

'''
Someone thinks that the soccer team is being robbed of goals each game and decides 
that they are going to count each goal from this team as 2 goals.

Uncomment num_goals_2 and set it equal to each value of num_goals multiplied by 2.

Then calculate and print the variance of num_goals_2 to see that the variance of 
num_goals_2 is equal to the variance of num_goals times two squared (same as times four).
'''

## Checkpoint 4
num_goals_2 = num_goals *2

print(np.var(num_goals_2))