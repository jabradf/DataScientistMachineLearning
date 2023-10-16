
from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2

#plot your other histogram here
#plt.hist(sales_times1, range=(55, 75), bins=20, alpha=0.5)
#plt.hist(sales_times1, range=(55, 75), bins=20, histtype='step') #outline plot
#plt.hist(sales_times1, bins=20, alpha=0.5, density=True) #density normalises the data
plt.hist(sales_times1, bins=20, alpha=0.4, density=True)
plt.hist(sales_times2, bins=20, alpha=0.4, density=True)

plt.show()