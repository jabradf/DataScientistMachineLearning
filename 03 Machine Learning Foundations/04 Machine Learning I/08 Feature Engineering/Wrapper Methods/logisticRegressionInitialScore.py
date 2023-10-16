import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the data
health = pd.read_csv("dataR2.csv")
print(health.head())
# Split independent and dependent variables
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Logistic regression model
lr = LogisticRegression(max_iter=1000)
'''
scikit-learn uses an algorithm that goes through many iterations to find optimal logistic regression coefficients. 
For this particular dataset, the algorithm doesn’t converge after the default maximum number of iterations, so we’ve 
included max_iter=1000 as a parameter in the LogisticRegression object just to make sure the algorithm converges
'''

# Fit the model
lr.fit(X,y)

# Print the accuracy of the model
print("score:",lr.score(X,y))