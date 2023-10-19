#import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

# Code Start here:
num_clusters = list(range(1,9))
inertias = []
#print(model.inertia_)
for i in num_clusters:
  model = KMeans(n_clusters=i, n_init='auto')
  model.fit(samples)
  inertias.append(model.inertia_)

plt.plot(num_clusters, inertias, '-o')

plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')

plt.show()



