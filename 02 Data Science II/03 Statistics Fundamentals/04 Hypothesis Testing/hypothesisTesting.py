'''
We have provided a small dataset called prices, representing the purchase 
prices of customers to BuyPie.com in the past day.

First, print out prices to the console and examine the numbers. How much 
variation is there in the purchase prices? Can you estimate the mean by looking at these numbers?
'''


'''
Calculate the mean of prices using np.mean(). Store it in a variable called prices_mean and print it out.

What is the average purchase price for these 50 purchases? Is it a lot less than 1000? Or only a little less?
'''
import numpy as np

prices = np.genfromtxt("prices.csv")

# print prices:
print(prices)
# calculate prices_mean and print it out:

prices_mean = np.mean(prices)
print(prices_mean)