One question to consider is how to choose the number of features to randomly select. Why did we choose 3 in this example? A good rule of thumb is select as many features as the square root of the total number of features. Our car dataset doesn’t have a lot of features, so in this example, it’s difficult to follow this rule. But if we had a dataset with 25 features, we’d want to randomly select 5 features to consider at every split point.


Here are some of the major takeaways about random forests:

* A random forest is an ensemble machine learning model. It makes a classification by aggregating the classifications of many decision trees.
* Random forests are used to avoid overfitting. By aggregating the classification of multiple trees, having overfitted trees in a random forest is less impactful.
* Every decision tree in a random forest is created by using a different subset of data points from the training set. Those data points are chosen at random with replacement, which means a single data point can be chosen more than once. This process is known as bagging.
* When creating a tree in a random forest, a randomly selected subset of features are considered as candidates for the best splitting feature. If your dataset has n features, it is common practice to randomly select the square root of n features.