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

# Sequential backward selection
sbs = SFS(lr,
          k_features=3,
          forward=False,
          floating=False,
          scoring='accuracy',
          cv=0)
sbs.fit(X, y)

# Print the chosen feature names
print(sbs.subsets_)
# Print the accuracy of the model after sequential backward selection
print("feature names:",sbs.subsets_[3]['feature_names'])
print("average score:", sbs.subsets_[3]['avg_score'])

# Plot the model accuracy
plot_sfs(sbs.get_metric_dict())
plt.show()
