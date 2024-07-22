# Introduction to Feature Selection Methods

Learn about the pros and cons of different feature selection methods.

# Introduction and motivation

Imagine you want to build a machine learning model for predicting the presence of a disease, and you have a dataset of patient records containing hundreds of different metrics, from demographic characteristics to medical test results to past treatment history. While having access to so many data points is always a good starting point, you most likely would not want to use all of the available features to construct your model, as many of them can be redundant or irrelevant, and would only serve to contribute unnecessary noise. Instead, a more effective approach is to select only a subset of relevant, predictive features to use in your model — this process is known as feature selection.

Feature selection is an important step in the machine learning pipeline, and when done right, can optimize the performance and predictive power of your model. The goal is to improve the model’s accuracy and efficiency by eliminating extraneous variables that do not contribute any useful information. In addition, simplifying the model through feature selection not only makes the results more easily interpretable, but also reduces the time and resources required to run the model.

There are three broad categories of feature selection that we will discuss in this article: filter methods, wrapper methods, and embedded methods.

# Feature Selection Methods
## Filter methods

Filter methods are the simplest type of feature selection method. They work by filtering features prior to model building based on some criteria.

### Advantages

* They are computationally inexpensive, since they do not involve testing the subsetted features using a model.
* They can work for any type of machine learning model.

### Disadvantages

* It is more difficult to take multivariate relationships into account because we are not evaluating model performance. For example, a variable might not have much predictive power on its own, but can be informative when combined with other variables.
* They are not tailored toward specific types of models.

### Examples

* Variance thresholds
* Correlation
* Mutual information

## Wrapper methods
Wrapper methods involve fitting a model and evaluating its performance for a particular subset of features. They work by using a search algorithm to find which combination of features can optimize the performance of a given model.
### Advantages

* They can determine the optimal set of features that produce the best results for a specific machine learning problem.
* They can better account for multivariate relationships because model performance is evaluated.

### Disadvantages

* They are computationally expensive because the model needs to be re-fitted for each feature set being tested.

### Examples

    Forward/backward/bidirectional sequential feature selection
    Recursive feature elimination

## Embedded methods

Embedded methods also involve building and evaluating models for different feature subsets, but their feature selection process happens at the same time as their model fitting step.
### Advantages

* Like wrapper methods, they can optimize the feature set for a particular model and account for multivariate relationships.
* They are also generally less computationally expensive because feature selection happens during model training.

### Examples

* Regularization (e.g., lasso/ridge regression)
* Tree-based feature importance

# Conclusion

When it comes to the number of features to keep for your model, more is not always better. It is worth being selective about which features to retain in order to maximize performance and reduce noise. Therefore, finding and implementing the right feature selection method is a key part of developing an effective and reliable model.
