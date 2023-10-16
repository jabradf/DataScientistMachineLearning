from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

x = range(len(drinks))
# Plot the bar graph here
plt.bar(x, ounces_of_milk, yerr=error, capsize=5)
plt.show()


###################

from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart her
plt.figure(figsize=(10,8))
x = range(len(years))
plt.bar(x, past_years_averages, yerr=error, capsize=5)
plt.axis([-0.5, 6.5, 70, 95])

ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)

plt.title('Final Exam Averages')
plt.ylabel('Test average')
plt.xlabel('Year')

plt.show()
plt.savefig('my_bar_chart.png')
