import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn 

## add code below
## read in csv file
cars = pd.read_csv('cars.csv')

## set you price variable
prices = cars.sellingprice

## plot a histogram of prices
plt.hist(prices, bins=150) # color = 'g'
plt.xticks(rotation=45)
plt.title('Car Prices')
plt.xlabel("Price")
plt.ylabel("count")
plt.show()

## log transform prices
log_prices = np.log(prices)

## plot a histogram of log_prices
plt.hist(log_prices, bins=150) # color = 'g'
plt.xticks(rotation=45)
plt.title('Logrithm of Car Prices')
plt.xlabel("Price")
plt.ylabel("count")
plt.show()