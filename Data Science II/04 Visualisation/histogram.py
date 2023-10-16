import codecademylib3
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


############################

import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Make your chart here

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(unit_topics) # Number of sets of bars
w = 0.8 # Width of each bar
#store1_x = [t*element + w*n for element in range(d)]
school_a_x = create_x(t, w, 1, d)
school_b_x = create_x(t, w, 2, d)

plt.figure(figsize=(10,8))

plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)

ax = plt.subplot()
middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.legend(["Middle School A", "Middle School B"])

plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test average')

plt.show()
plt.savefig('my_side_by_side.png')


######################################

import codecademylib
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
#create your plot here
plt.figure(figsize=(10,8))
plt.bar(x, As, label="As")
plt.bar(x, Bs, bottom=As, label="Bs")
plt.bar(x, Cs, bottom=c_bottom, label="Cs")
plt.bar(x, Ds, bottom=d_bottom, label="Ds")
plt.bar(x, Fs, bottom=f_bottom, label="Fs")

ax = plt.subplot()
ax.set_xticks(x)
ax.set_xticklabels(unit_topics)
plt.xlabel('Unit')
plt.ylabel('Number of Students')
plt.title("Grade Distribution")

plt.show()
plt.savefig('my_stacked_bar.png')


#####################################import codecademylib3
from matplotlib import pyplot as plt

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]

# Make your plot here
plt.figure(figsize=(10,8))
plt.hist(exam_scores1, bins=12, alpha=0.4, density=True, histtype='step', linewidth=2)
plt.hist(exam_scores2, bins=12, alpha=0.4, density=True, histtype='step', linewidth=2)

plt.title("Final Exam Score Distribution")
plt.legend(["1st Yr Teaching", "2nd Yr Teaching"])
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.show()
plt.savefig('my_histogram.png')