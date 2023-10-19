Basic filtering is dropping features:

X = df.drop(columns=['exam_score'])


# Variance Threshold
Drop features from a temporary dataframe. Default drops data with zero variance:

from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0)  # 0 is default
print(selector.fit_transform(X_num))


# Pearson's correlation
Another type of filter method involves finding the correlation between variables. In particular, the Pearson’s correlation coefficient is useful for measuring the linear relationship between two numeric, continuous variables — a coefficient close to 1 represents a positive correlation, -1 represents a negative correlation, and 0 represents no correlation. Like variance, Pearson’s correlation coefficient cannot be calculated for categorical variables. Although, there is a related point biserial correlation coefficient that can be computed when one variable is dichotomous, but we won’t focus on that here.

When two features are highly correlated with one another, then keeping just one to be used in the model will be enough because otherwise they provide duplicate information. The second variable would only be redundant and serve to contribute unnecessary noise.

Get correlation matrix by generating the heatmap:

import matplotlib.pyplot as plt
import seaborn as sns
corr_matrix = X_num.corr(method='pearson')  # 'pearson' is default
sns.heatmap(corr_matrix, annot=True, cmap='RdBu_r')
plt.show()

Let’s define high correlation as having a coefficient of greater than 0.7 or less than -0.7. We can loop through the correlation matrix to identify the highly correlated variables:

# Loop over bottom diagonal of correlation matrix
for i in range(len(corr_matrix.columns)):
    for j in range(i):
 
        # Print variables with high correlation
        if abs(corr_matrix.iloc[i, j]) > 0.7:
            print(corr_matrix.columns[i], corr_matrix.columns[j], corr_matrix.iloc[i, j])


Output is
hours_TV hours_study -0.780763315142435

As seen, hours_TV appears to be highly negatively correlated with hours_study — a student who watches a lot of TV tends to spend fewer hours studying, and vice versa. Because they provide redundant information, we can choose to remove one of those variables. To decide which one, we can look at their correlation with the target variable, then remove the one that is less associated with the target. This is explored in the next section.


# Correlation between feature and target
As mentioned, the second way correlation can be used is to determine if there is a relationship between a feature and the target variable. In the case of Pearson’s correlation, this is especially useful if we intend to fit a linear model, which assumes a linear relationship between the target and predictor variables. If a feature is not very correlated with the target variable, such as having a coefficient of between -0.3 and 0.3, then it may not be very predictive and can potentially be filtered out.

We can use the same .corr() method seen previously to obtain the correlation between the target variable and the rest of the features. First, we’ll need to create a new DataFrame containing the numeric features with the exam_score column:

X_y = X_num.copy()
X_y['exam_score'] = y
print(X_y)


Generate the correlation matrix and isolate the column corresponding to the target variable:

corr_matrix = X_y.corr()
# Isolate the column corresponding to `exam_score`
corr_target = corr_matrix[['exam_score']].drop(labels=['exam_score'])
sns.heatmap(corr_target, annot=True, fmt='.3', cmap='RdBu_r')
plt.show()


Drop the column that is negatively related (standard, but can be the positive one)

X = X.drop(columns=['hours_TV'])
print(X)


The other two features, hours_sleep and height_cm, both do not seem to be correlated with exam_score, suggesting they would not be very good predictors. We could potentially remove either or both of them as being uninformative. But before we do, it is a good idea to use other methods to double check that the features truly are not predictive. We will do that in the next section by using mutual information to see if there are any non-linear associations between the features and target variable.



To conclude this section, we’ll briefly note an alternative approach for assessing the correlation between variables. Instead of generating the full correlation matrix, we could use the f_regression() function from scikit-learn to find the F-statistic for a model with each predictor on its own. The F-statistic will be larger (and p-value will be smaller) for predictors that are more highly correlated with the target variable, thus it will perform the same filtering:

from sklearn.feature_selection import f_regression
print(f_regression(X_num, y))

(array([3.61362007e+01, 3.44537037e+01, 0.00000000e+00, 1.70259066e-03]),
 array([3.19334945e-04, 3.74322763e-04, 1.00000000e+00, 9.68097878e-01]))

The function returns the F-statistic in the first array and the p-value in the second. As seen, the result is consistent with what we had observed in the correlation matrix — the stronger the correlation (either positive or negative) between the feature and target, the higher the corresponding F-statistic and lower the p-value. For example, amongst all the features, hours_study has the largest correlation coefficient (0.905), highest F-statistic (3.61e+01), and lowest p-value (3.19e-04).

# Mutual information
The final filter method we’ll look at is using mutual information to rank and select the top features. Mutual information is a measure of dependence between two variables and can be used to gauge how much a feature contributes to the prediction of the target variable. It is similar to Pearson’s correlation, but is not limited to detecting linear associations. This makes mutual information useful for more flexible models where a linear functional form is not assumed. Another advantage of mutual information is that it also works on discrete features or target, unlike correlation. Although, categorical variables need to be numerically encoded first.

In our example, we can encode the edu_goal column using the LabelEncoder class from scikit-learn‘s preprocessing module:

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
# Create copy of `X` for encoded version
X_enc = X.copy()
X_enc['edu_goal'] = le.fit_transform(X['edu_goal'])
print(X_enc)
 

Now, we can compute the mutual information between each feature and exam_score using mutual_info_regression(). This function is used because our target variable is continuous, but if we had a discrete target variable, we would use mutual_info_classif(). We specify the random_state in the function in order obtain reproducible results:

from sklearn.feature_selection import mutual_info_regression
print(mutual_info_regression(X_enc, y, random_state=68))
 
#output:
[0.50396825 0.40896825 0.06896825 0.        ]
 

The estimated mutual information between each feature and the target is returned in a numpy array, where each value is a non-negative number — the higher the value, the more predictive power is assumed.

However, we are missing one more important piece here. Earlier, even though we encoded edu_goal to be numeric, that does not mean it should be treated as a continuous variable. In other words, the values of edu_goal are still discrete and should be interpreted as such. If we plot edu_goal against exam_score on a graph, we can clearly see the steps between the values of edu_goal:

In order to properly calculate the mutual information, we need to tell mutual_info_regression() which features are discrete by providing their index positions using the discrete_features parameter:


print(mutual_info_regression(X_enc, y, discrete_features=[0], random_state=68))
 
#output:
[0.75563492 0.38896825 0.18563492 0.        ]



Compared to the earlier results, we now get greater mutual information between edu_goal and the target variable once it is correctly interpreted as a discrete feature.

From the results, we can also see that there is 0 mutual information between height_cm and exam_score, suggesting that these variables are largely independent. This is consistent with what we saw earlier with Pearson’s correlation, where the correlation coefficient between them is very close to 0 as well.

What is interesting to note is that the mutual information between hours_sleep and exam_score is a positive value, even though their Pearson’s correlation coefficient is 0. The answer becomes more clear when we plot the relationship between hours_sleep and exam_score:

As seen, there do seem to be some association between the variables, only it is not a linear one, which is why it was detected using mutual information but not Pearson’s correlation coefficient.

Finally, let’s look at using the SelectKBest class from scikit-learn to help pick out the top k features with the highest ranked scores. In our case, we are looking to select features that share the most mutual information with the target variable. When we instantiate SelectKBest, we’ll specify which scoring function to use and how many top features to select. Here, our scoring function is mutual_info_regression(), but because we want to specify additional arguments besides the X and y inputs, we’ll need the help of the partial() function from Python’s built-in functools module. Then, the .fit_transform() method will return the filtered features as a numpy array:

from sklearn.feature_selection import SelectKBest
from functools import partial
score_func = partial(mutual_info_regression, discrete_features=[0], random_state=68)
# Select top 3 features with the most mutual information
selection = SelectKBest(score_func=score_func, k=3)
print(selection.fit_transform(X_enc, y))

#output:
[[ 0  1 10]
 [ 0  2 10]
 [ 0  3  8]
 [ 1  3  8]
 [ 1  3  6]
 [ 1  4  6]
 [ 1  3  8]
 [ 2  4  8]
 [ 2  5 10]
 [ 2  5 10]]
 


As seen above, we selected the top 3 features based on mutual information, thus dropping height_cm. Like VarianceThreshold, SelectKBest also offers the .get_support() method that returns the indices of the selected features, so we could subset our original features DataFrame:

X = X[X.columns[selection.get_support(indices=True)]]
print(X)
 

edu_goal	hours_study	hours_sleep
bachelors	1	10
bachelors	2	10
bachelors	3	8
masters		3	8
masters		3	6
masters		4	6
masters		3	8
phd		4	8
phd		5	10
phd		5	10

# Conclusion
In our example dataset, we started out with 6 features for predicting the exam_score of students. Using various filter methods, we narrowed down that set to just the top most relevant and informative ones. First, we eliminated grade_level because it has zero variance and would contribute nothing to the model. Then, we dropped hours_TV since it is highly correlated with hours_study and is therefore redundant. Lastly, we filtered out height_cm based on mutual information, which suggested that it does not have any meaningful association with the target variable, linear or otherwise, and would not have been very predictive.

Phew! That was a lot we were able to accomplish using filter methods. Being the most simple type of feature selection method, they sure do not lack power nor potential. It is certainly worth considering how you might want to incorporate filter methods into your next machine learning project.