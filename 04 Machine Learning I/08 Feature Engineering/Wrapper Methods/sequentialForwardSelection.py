import pandas as pd
#import codecademylib3
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt

# Load the data
health = pd.read_csv("dataR2.csv")
X = health.iloc[:,:-1]
y = health.iloc[:,-1]

# Logistic regression model
lr = LogisticRegression(max_iter=1000)

# Sequential forward selection
sfs = SFS(lr,
          k_features=9,
          forward=True,
          floating=False,
          scoring='accuracy',
          cv=0)
# cv allows you to do k-fold cross-validation. We’ll leave it at 0 for this lesson and only evaluate performance on the training set.
sfs.fit(X, y)

# Print the chosen feature names
print(sfs.subsets_)
# Print the accuracy of the model after sequential forward selection

# Plot the model accuracy
plot_sfs(sfs.get_metric_dict())
plt.show()