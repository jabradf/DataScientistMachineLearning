import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler

# Load the data
health = pd.read_csv("dataR2.csv")
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Create a list of feature names
feature_list = list(X.columns)

# Standardize the data
X = StandardScaler().fit_transform(X)

# Logistic regression
lr = LogisticRegression(max_iter=1000)

# Recursive feature elimination
rfe = RFE(estimator=lr, n_features_to_select=3)
rfe.fit(X, y)

# List of features chosen by recursive feature elimination
rfe_features = [f for (f, support) in zip(feature_list, rfe.support_) if support]
print(rfe_features)
print(rfe.ranking_)
'''
A 1 at a certain index indicates that recursive feature elimination kept the feature at the same index. In this example, the model kept the features at indices 3 and 5: Rain and FWI. The other numbers indicate at which step a feature was removed. The 5 (the highest rank in the array) at index 1 means that RH (the feature at index 1) was removed first. The 4 at index 2 means that Ws (the feature at index 2) was removed in the next step, and so on.
'''

print(rfe.support_)
'''
rfe.support_ is an array with True and False values that indicate which features were chosen. Here’s an example of what this looks like, again using the fire dataset.
'''


# Print the accuracy of the model with features chosen by recursive feature elimination
print("score:",rfe.score(X, y))
