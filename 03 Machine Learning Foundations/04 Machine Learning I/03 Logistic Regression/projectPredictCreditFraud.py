import seaborn
import pandas as pd
import numpy as np
#import codecademylib3
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data
transactions = pd.read_csv('transactions_modified.csv')
print(transactions.head())
print(transactions.info())

# How many fraudulent transactions?
counts = transactions.isFraud.value_counts()
print("There are " + str(counts[1]) + " cases of fraud.")

# Summary statistics on amount column
print(transactions.amount.describe())


# Create isPayment field
transactions['isPayment'] = 0
transactions['isPayment'][transactions['type'].isin(['PAYMENT','DEBIT'])] = 1

# Create isMovement field
transactions['isMovement'] = 0
transactions['isMovement'][transactions['type'].isin(['CASH_OUT','TRANSFER'])] = 1

# Create accountDiff field
transactions['accountDiff'] = transactions.oldbalanceOrg - transactions.oldbalanceDest

# Create features and label variables
features = transactions[['amount', 'isPayment', 'isMovement', 'accountDiff']]
label = transactions['isFraud']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state = 27)

# Normalize the features variables
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Fit the model to the training data
model = LogisticRegression()
model.fit(X_train,y_train)


# Score the model on the training data
score_train = model.score(X_train, y_train)
print("Training score:", score_train)

# Score the model on the test data
score_test = model.score(X_test, y_test)
print("Testing score:", score_test)

# Print the model coefficients
model_coeff = model.coef_
print(model_coeff)


# New transaction data
# (remember: amount, isPayment, isMovement, difference)
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])

# Create a new transaction
new_trans = np.array([500000.01, 1.0, 0.0, 9805.01])

# Combine new transactions into a single array
sample_transactions = np.stack((transaction1, transaction2, transaction3, new_trans))
print(sample_transactions)

# Normalize the new transactions
sample_transactions = scaler.transform(sample_transactions)

# Predict fraud on the new transactions
newTransPred = model.predict(sample_transactions)
print("New predictions: ", newTransPred)

# Show probabilities on the new transactions
probabilities = model.predict_proba(sample_transactions)
print(probabilities)
#1st column prob not fraudulent, 2nd column fraudulent