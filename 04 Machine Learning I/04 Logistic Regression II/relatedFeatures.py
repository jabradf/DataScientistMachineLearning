import pandas as pd
import numpy as np
#import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

#https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})
predictor_var = ['radius_mean', 'texture_mean', 'perimeter_mean','area_mean', 'smoothness_mean', 'compactness_mean','concavity_mean', 'symmetry_mean', 'fractal_dimension_mean']
x = df[predictor_var]

#Compare the curves
sns.regplot(x= 'radius_mean', y= 'diagnosis', data= df, logistic= True,)
plt.show()
plt.close()
sns.regplot(x= 'fractal_dimension_mean', y= 'diagnosis', data= df, logistic= True)
plt.show()
plt.close()

#1 Uncomment the heatmap and identify the two features that are highly correlated with radius_mean.
plt.figure(figsize = (10,7))
sns.heatmap(x.corr(), annot=True)
plt.show()

#2. Identify the other highly correlated pair. Define an array called correlated_pair containing the two features you've identified.
correlated_pair = ['concavity_mean', 'compactness_mean']