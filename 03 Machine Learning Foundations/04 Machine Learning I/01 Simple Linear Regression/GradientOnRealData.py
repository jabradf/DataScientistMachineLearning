import codecademylib3_seaborn
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

plt.plot(X, y, 'o')
#plot your line here:
num_iterations = 100 #1000
learning_rate = 0.0001
b, m = gradient_descent(X, y, learning_rate, num_iterations)
y_predictions = [m*element + b for element in X]

plt.plot(X, y_predictions)

plt.show()




