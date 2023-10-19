import numpy as np

a = "spam"
b = "enhancement"

p_spam = 0.2

p_enhancement_given_spam = 0.05

p_enhancement = p_enhancement_given_spam * p_spam + 0.001 * (1-p_spam)

p_spam_enhancement = p_enhancement_given_spam * p_spam / p_enhancement
print(p_spam_enhancement)


# quiz:
posTotal = 2+1+3+2
negTotal = 1+7+2+2

print(posTotal)
print(negTotal)

print('---')
print((2+1)/(posTotal+negTotal))