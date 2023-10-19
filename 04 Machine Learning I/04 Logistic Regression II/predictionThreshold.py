import pandas as pd
import numpy as np

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv('breast_cancer_data.csv')
#encode malignant as 1, benign as 0
df['diagnosis'] = df['diagnosis'].replace({'M':1,'B':0})
predictor_var = ['radius_mean', 'texture_mean', 
                  'compactness_mean',
                 'symmetry_mean',]
outcome_var='diagnosis'
x_train, x_test, y_train, y_test = train_test_split(df[predictor_var], df[outcome_var], random_state=0, test_size=0.3)


log_reg = LogisticRegression(penalty='none', fit_intercept=True,tol=0.0000001,solver='newton-cg')
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)
y_pred_prob = log_reg.predict_proba(x_test)



#Using the predicted probabilities to get the predicted class
y_pred_class = (y_pred_prob[:,1]>0.5)*1.0
#1 Check if it's the same as y_pred
diff = np.array_equal(y_pred, y_pred_class)
print("Is equal:", diff)

## 2. Print the confusion matrix
print("Confusion Matrix: Threshold 50%")
cm_50 = confusion_matrix( y_test, y_pred_class)
print(cm_50)

##3 Confusion matrices for thresholds of 0.25 and 0.75
print("Confusion Matrix: Threshold 25%")
y_pred_class = (y_pred_prob[:,1]>0.25)*1.0
cm_25 = confusion_matrix( y_test, y_pred_class)
print(cm_25)

y_pred_class = (y_pred_prob[:,1]>0.75)*1.0
cm_75 = confusion_matrix(y_test, y_pred_class)
print("Confusion Matrix: Threshold 75%")
print(cm_75)


#4. Choosing the right threshold for a question

#Array of thresholds
thresh = np.linspace(0,1,100)
false_negatives = []

result = 9999
for t in thresh:
  cm = confusion_matrix(y_test, (y_pred_prob[:,1]>t)*1.0)
  false_negatives.append(cm[1][0])
  if result==9999 and cm[1][0] >= 2:
    result = t

thresh_choice = result
print(thresh_choice)

# official solution
#temp = thresh[np.argmax(np.array(false_negatives)>=2)]
#print(temp)
