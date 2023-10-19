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
                 'symmetry_mean',]
outcome_var='diagnosis'
x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=0, test_size=0.3)

#1. Fit a Logistic Regression model with the specified hyperparameters
log_reg = LogisticRegression(penalty='none', fit_intercept=True)
print(log_reg.get_params())


#2. Fit the model to training data and obtain cofficient and intercept
log_reg.fit(x_train, y_train)
coefficients = log_reg.coef_
print("coefficients: ", coefficients)
intercept = log_reg.intercept_
print("intercept: ", intercept)

#3. Calculate the accuracy, precision, recall, and f1-score on the testing data
y_pred = log_reg.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Test set accuracy:\t{accuracy}')
print(f'Test set precision:\t{precision}')
print(f'Test set recall:\t{recall}')
print(f'Test set f1-score:\t{f1}')

#4. Remove the comments from the following code block to print the confusion matrix
test_conf_matrix = pd.DataFrame(
     confusion_matrix(y_test, y_pred), 
     index=['actual no', 'actual yes'], 
     columns=['predicted no', 'predicted yes']
     )

print(test_conf_matrix)
