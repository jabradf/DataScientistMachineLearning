import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
#import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

data_matrix_standardized = pd.read_csv('data_matrix_standardized.csv')
classes = pd.read_csv('classes.csv')['Class']

# 1. Transform the data into 4 new features using the first PCs
pca = PCA(n_components = 4)
data_pcomp = pca.fit_transform(data_matrix_standardized)
data_pcomp = pd.DataFrame(data_pcomp)
data_pcomp.columns = ['PC1', 'PC2', 'PC3', 'PC4']
print(data_pcomp.head())

## 2. Plot the first two principal components colored by the bean classes
data_pcomp['bean_classes'] = classes
sns.lmplot(x='PC1', y='PC2', data=data_pcomp, hue='bean_classes', fit_reg=False)
plt.show()