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
predictor_var = ['radius_mean', 'texture_mean', 
                  'compactness_mean',
                 'symmetry_mean']
outcome_var='diagnosis'

x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=6, test_size=0.3)

print('Train positivity rate: ')
print(sum(y_train)/y_train.shape[0])
print('Test positivity rate: ')
print(sum(y_test)/y_test.shape[0])

log_reg = LogisticRegression(penalty='none', max_iter=1000, fit_intercept=True, tol=0.000001)
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)

recall = recall_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print('Recall and Accuracy scores')
print(recall, accuracy)

## 1. Stratified Sampling
#stratify means to ensure the split retains the same % results as the entire example set. Use the outcome to stratify the data.
x_train_str, x_test_str, y_train_str, y_test_str = train_test_split(df[predictor_var], df[outcome_var], random_state=6, test_size=0.3, stratify=df[outcome_var])

### 2. Stratified positivity rates
print('Stratified train positivity rate: ')
str_train_positivity_rate = sum(y_train_str)/y_train_str.shape[0]
print(str_train_positivity_rate)
print('Stratified test positivity rate: ')
str_test_positivity_rate = sum(y_test_str)/y_test_str.shape[0]
print(str_test_positivity_rate)

### 3. Model predictions after Stratified sampling 
log_reg.fit(x_train_str, y_train_str)
y_pred_str = log_reg.predict(x_test_str)

recall_str = recall_score(y_test_str, y_pred_str)
accuracy_str = accuracy_score(y_test_str, y_pred_str)

print('Stratified Sampling: Recall and Accuracy scores')
print(recall_str, accuracy_str)

### 4. Balanced Class Weights
log_reg_bal = LogisticRegression(penalty='none', max_iter=1000, fit_intercept=True, tol=0.000001, class_weight='balanced')

### 5. Model Predictions after balancing Class Weights
log_reg_bal.fit(x_train, y_train)
y_pred_bal = log_reg_bal.predict(x_test)
recall_bal = recall_score(y_test, y_pred_bal)
accuracy_bal = accuracy_score(y_test, y_pred_bal)

print('Balanced Class Weights: Recall and Accuracy scores')
print(recall_bal, accuracy_bal)