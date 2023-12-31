# Import pandas and the data
import pandas as pd
codecademyU = pd.read_csv('codecademyU_2.csv')

# Separate out X and y
X = codecademyU[['hours_studied', 'practice_test']]
y = codecademyU.passed_exam

# Transform X
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 27)

# Create and fit the logistic regression model here:
from sklearn.linear_model import LogisticRegression
cc_lr = LogisticRegression()
cc_lr.fit(X_train, y_train)

# Print the intercept and coefficients here:
print("coeff: ", cc_lr.coef_)
print("intercept: ", cc_lr.intercept_)


# Print out the predicted outcomes for the test data
pred = cc_lr.predict(X_test)
print(pred)
# Print out the predicted probabilities for the test data
prob = cc_lr.predict_proba(X_test)
print(prob)
# Print out the true outcomes for the test data
print(y_test)