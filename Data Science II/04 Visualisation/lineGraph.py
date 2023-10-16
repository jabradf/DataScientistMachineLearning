from matplotlib import pyplot as plt

x = range(0, 5)
y1 = [123.463,456,43,23,23]
y2 = [33, 44, 55, 11, 33]

plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.legend(['Y1', 'Y2'], loc=4)
plt.show()