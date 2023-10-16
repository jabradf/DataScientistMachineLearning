'''
A certain basketball player has an 85% chance of making a given free throw and takes 20 free throws.

Uncomment expected_baskets and set it equal to the number of free throws they are expected to make.

Then print expected_baskets.
'''

## Checkpoint 1
expected_baskets = 20 * 0.85
print(expected_baskets)


'''
Let’s say a student has a 98% chance of arriving early 
or on time to class. Uncomment the variable called expected_late 
and set it equal to the expected number of times the student will 
arrive late to class throughout the 180 school days in a school year.
'''
## Checkpoint 2
expected_late = (1-0.98) * 180
print(expected_late)


########################
'''
A certain basketball player has an 85% chance of making a given free throw. 
Uncomment variance_baskets and set it equal to the variance of free throws made from 20 shots.
'''


## Checkpoint 1
variance_baskets = 20 * 0.85 * (1-0.85)
print(variance_baskets)


'''
Let’s say a student has a 98% chance of arriving on time 
to class. Uncomment variance_late and set it equal to the variance of 
days the student will arrive late to class throughout the 180 school days in a school year.
'''
## Checkpoint 2
variance_late = 180 * 0.02 * (1-0.02)
print(variance_late)