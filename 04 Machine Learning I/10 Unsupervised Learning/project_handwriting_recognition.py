#import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()
#print(digits.target)

#plt.gray()
#plt.matshow(digits.images[100])
#plt.show()
#print(digits.target[100])

from sklearn.cluster import KMeans
k=10  # 10 digits
model = KMeans(k, random_state=42, n_init='auto')
model.fit(digits.data)
fig = plt.figure(figsize=(8,3))
plt.suptitle("title here", fontsize=13, fontweight='bold')

for i in range(10):
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)
  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()

new_samples = np.array([
[0.00,0.15,2.06,3.05,2.21,0.00,0.00,0.00,0.00,5.04,7.63,7.63,7.63,2.98,0.00,0.00,0.00,5.57,3.82,0.54,5.72,7.01,0.15,0.00,0.00,0.00,0.00,0.00,2.44,7.63,1.83,0.00,0.00,0.00,0.00,0.00,3.97,7.63,2.14,0.00,0.00,0.15,1.53,5.27,7.63,4.88,0.08,0.00,2.44,6.64,7.63,7.25,3.59,0.38,1.14,0.00,7.24,7.63,7.63,7.63,6.71,6.94,7.47,0.15],
[0.00,0.00,0.00,2.90,2.29,0.00,0.00,0.00,0.00,0.00,0.00,6.10,5.34,0.00,0.00,0.00,0.00,0.00,0.00,6.10,5.34,0.00,0.00,0.00,0.00,0.00,0.00,6.10,5.34,0.00,0.00,0.00,0.00,0.00,0.00,6.10,5.34,0.00,0.00,0.00,0.00,0.00,0.00,6.02,5.11,0.00,0.00,0.00,0.00,0.00,0.00,1.14,0.92,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,5.34,6.03,1.15,0.08,0.00,0.00,0.00,0.00,5.34,6.71,7.55,3.13,0.00,0.00,0.00,0.00,5.35,6.26,6.63,5.18,0.00,0.00,0.00,0.00,4.19,7.40,6.18,5.87,1.15,2.29,2.29,0.00,1.75,7.63,7.55,7.62,7.63,7.63,7.62,0.00,0.00,2.75,7.09,6.33,2.74,1.30,0.76,0.00,0.00,0.00,6.79,4.82,0.00,0.00,0.00,0.00,0.00,0.00,5.64,4.73,0.00,0.00,0.00],
[0.00,2.22,5.04,4.96,1.99,0.00,0.00,0.00,0.46,7.55,6.86,6.94,7.55,2.67,0.00,0.00,0.08,3.36,0.69,0.23,5.95,6.49,0.00,0.00,0.00,0.00,0.00,0.76,6.33,6.48,0.00,0.00,0.00,2.14,6.56,7.55,7.25,2.06,0.00,0.00,0.00,6.18,7.63,6.80,4.04,3.05,2.59,0.00,0.00,5.80,7.63,7.63,7.63,7.63,7.17,0.16,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
])

new_labels = model.predict(new_samples)
print(new_labels)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
