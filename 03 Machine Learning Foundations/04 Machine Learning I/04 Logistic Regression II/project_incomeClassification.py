import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler

#import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns


col_names = ['age', 'workclass', 'fnlwgt','education', 'education-num', 
'marital-status', 'occupation', 'relationship', 'race', 'sex',
'capital-gain','capital-loss', 'hours-per-week','native-country', 'income']
df = pd.read_csv('adult.data',header = None, names = col_names)

#Clean columns by stripping extra whitespace for columns of type "object"
for c in df.select_dtypes(include=['object']).columns:
    df[c] = df[c].str.strip()
print(df.head())

#1. Check Class Imbalance
print(df.income.value_counts(normalize=True))

#2. Create feature dataframe X with feature columns and dummy variables for categorical features
feature_cols = ['age','capital-gain', 'capital-loss', 'hours-per-week', 'sex','race', 'hours-per-week', 'education']
# ensure drop_first is there to eliminate colinear features
X = pd.get_dummies(df[feature_cols], drop_first=True)


#3. Check logistic regression assumption: feature correlation
plt.figure()
sns.heatmap(X.corr())
plt.show()
plt.close()

#4. Create output variable y which is binary, 0 when income is less than 50k, 1 when it is greather than 50k
y = np.where(df.income=='<=50K', 0, 1)

#5a. Split data into a train and test set
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.3)

#5b. Fit LR model with sklearn on train set, and predicting on the test set
log_reg = LogisticRegression(C=0.05, penalty='l1', solver='liblinear')
log_reg.fit(x_train, y_train)


#6. Print model parameters and coefficients
intercept = log_reg.intercept_[0]
coefficients = log_reg.coef_
print('Model Parameters, Intercept:',intercept)
print('Model Parameters, Coeff:')
print(coefficients)

#7. Evaluate the predictions of the model on the test set. Print the confusion matrix and accuracy score.
y_pred = log_reg.predict(x_test)
test_conf_matrix = pd.DataFrame(
     confusion_matrix(y_test, y_pred), 
     index=['actual no', 'actual yes'], 
     columns=['predicted no', 'predicted yes']
     )
accuracy = accuracy_score(y_test, y_pred)

print('Confusion Matrix on test set:')
print(test_conf_matrix)
print('Accuracy Score on test set:', accuracy)

# 8.Create new DataFrame of the model coefficients and variable names; sort values based on coefficient
coef_df = pd.DataFrame(zip(x_train.columns, log_reg.coef_[0]), columns=['var', 'coef'])
coef_df = coef_df[coef_df.coef.abs()>0].sort_values('coef')
print(coef_df)

#9. barplot of the coefficients sorted in ascending order
sns.barplot(data=coef_df, x='var', y='coef')
plt.xticks(rotation=45);
plt.title('LR Coefficient Values')
plt.show()

#10. Plot the ROC curve and print the AUC value.
#y_pred_prob = log_reg.predict_proba(x_test)
y_pred_prob = log_reg.predict_proba(x_test)
fpr, tpr, thresholds = roc_curve(y_test,y_pred_prob[:,1])
plt.figure()
plt.plot(fpr, tpr, color='darkorange',
         label='ROC curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.plot([0,1],[0,1], color='blue',linestyle='--')
plt.title('ROC Curve')
plt.grid()
plt.show()



roc_auc = roc_auc_score(y_test, y_pred_prob[:,1])
print(f'ROC AUC score: {roc_auc}')