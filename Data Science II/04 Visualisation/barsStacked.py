
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

x=range(len(drinks))
plt.bar(x, sales1, label="Location 1")
plt.bar(x, sales2, bottom=sales1, label="Location 2")

plt.legend()
plt.show()