import pandas as pd
from sklearn.decomposition import PCA
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
 
'''
Read through the code to make sure that you understand what’s happening. Here are the steps:

Transform the original data by projecting it onto the first four principal axes. We chose four PCs because we previously 
found that they contain 95% of the variance in the original data
Split the data into 67% training and 33% testing sets
Use the transformed training data to fit an SVM model
Print out the average likelihood score for the testing data
Re-split the original 16 standardized features into training and test sets
Fit the same SVM model on the training set with all 16 features
Print out the average likelihood score for the test data
Notice that the score for the model using the first 4 principal components is higher than for the model that was fit with 
the 16 original features. We only needed 1/4 of the data to get even better model performance!
'''

data_matrix_standardized = pd.read_csv('./data_matrix_standardized.csv')
classes = pd.read_csv('classes.csv')
 
# We will use the classes as y
y = classes.Class.astype('category').cat.codes
 
# Get principal components with 4 features and save as X
pca_1 = PCA(n_components=4) 
X = pca_1.fit_transform(data_matrix_standardized) 
 
# Split the data into 33% testing and the rest training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
 
# Create a Linear Support Vector Classifier
svc_1 = LinearSVC(random_state=0, tol=1e-5)
svc_1.fit(X_train, y_train) 
 
# Generate a score for the testing data
score_1 = svc_1.score(X_test, y_test)
print(f'Score for model with 4 PCA features: {score_1}')
 
# Split the original data intro 33% testing and the rest training
X_train, X_test, y_train, y_test = train_test_split(data_matrix_standardized, y, test_size=0.33, random_state=42)
 
# Create a Linear Support Vector Classifier
svc_2 = LinearSVC(random_state=0)
svc_2.fit(X_train, y_train)
 
# Generate a score for the testing data
score_2 = svc_2.score(X_test, y_test)
print(f'Score for model with original features: {score_2}')
