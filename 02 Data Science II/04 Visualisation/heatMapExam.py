import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
 
# load in data
sales_data = pd.read_csv("sales_data.csv")
 
# calculate total sales for each month
sales = sales_data.groupby(["year", "month"]).sum()
 
# re-format the data for the heat-map
sales_month_year = sales.reset_index().pivot(index="year", columns="month", values="sales")
 
# create heatmap
sns.heatmap(sales_month_year, cbar_kws={"label": "month"})
plt.title("Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Year")
plt.show()