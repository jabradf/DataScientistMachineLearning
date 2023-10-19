#import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd

iris = datasets.load_iris()

samples = iris.data

target = iris.target

model = KMeans(n_clusters=3)

model.fit(samples)

labels = [iris.target_names[s] for s in model.predict(samples)]

# Code starts here:
species = [iris.target_names[t] for t in list(target)]

df = pd.DataFrame({'labels': labels, 'species': species})

print(df)

ct = pd.crosstab(df['labels'], df['species'])
print(ct)