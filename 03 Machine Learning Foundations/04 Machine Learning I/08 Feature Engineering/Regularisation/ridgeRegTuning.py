import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
df = pd.read_csv('student_math.csv')
print(df.shape)

y = df['Final_Grade']
X = df.drop(columns = ['Final_Grade'])

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV


#Create an array of alpha values between 0.01 and 10000
alpha_array = np.logspace(-2, 4, 100)


#Create a dictionary with a single key, alpha and values set to alpha_array
tuned_parameters = [{'alpha': alpha_array}]

# Perform GridSearchCV with Ridge regularization on the data
from sklearn.model_selection import GridSearchCV
model = GridSearchCV(estimator = Ridge(), param_grid = tuned_parameters, scoring = 'neg_mean_squared_error', cv=5, return_train_score = True)
model.fit(X, y)

# Print the tuned alpha and the best test score corresponding to it
test_scores = model.cv_results_['mean_test_score']
train_scores = model.cv_results_['mean_train_score']
print(model.best_params_, model.best_score_)
