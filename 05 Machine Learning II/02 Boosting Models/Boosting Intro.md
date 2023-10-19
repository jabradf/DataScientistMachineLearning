While boosting can be applied to any base machine learning algorithm, we will demonstrate with an extremely
 popular choice as a base estimator, the decision tree. Recall that Decision Trees are a commonly used 
 and powerful machine learning algorithm because they are easy to interpret. Additionally, the training 
 data requires very little manipulation (no need standardization, removal of collinearity, etc.).

The major limitation to decision trees is that they tend to suffer from high variance and are therefore 
prone to overfitting. They are good at making a series of decisions which cause them to memorize the 
training data, so they do not generalize well to unseen data. In the following exercises we will explore 
how to work past these limitations while using decision trees for boosting.


# Boosting
In this module we will cover a powerful ensemble method called Boosting. Boosted ensemble methods use weak learners as base models that are simple and tend to suffer from high bias. The weak learners underfit the data.

Boosting is a sequential learning technique where each of the base models builds off of the previous model. Each subsequent model aims to improve the performance of the final ensemble model by attempting to fix the errors in the previous stage.

There are two important decisions that need to be made to perform boosted ensembling:

Sequential Fitting Method
Aggregation Method
Two boosting algorithms that will be covered in detail in this module are Adaptive Boosting and Gradient Boosting.

While boosting can be applied to any base machine learning algorithm, we will demonstrate with an extremely popular choice as a base estimator, the decision tree. Recall that Decision Trees are a commonly used and powerful machine learning algorithm because they are easy to interpret. Additionally, the training data requires very little manipulation (no need standardization, removal of collinearity, etc.).

The major limitation to decision trees is that they tend to suffer from high variance and are therefore prone to overfitting. They are good at making a series of decisions which cause them to memorize the training data, so they do not generalize well to unseen data. In the following exercises we will explore how to work past these limitations while using decision trees for boosting.

# Adaptive Boosting Overview
Adaptive Boosting (or AdaBoost) is a sequential ensembling method that can be used for both classification and regression. It can use any base machine learning model, though it is most commonly used with decision trees.

For AdaBoost, the Sequential Fitting Method is accomplished by updating the weight attached to each of the training dataset observations as we proceed from one base model to the next. The Aggregation Method is a weighted sum of those base models where the model weight is dependent on the error of that particular estimator.

The training of an AdaBoost model is the process of determining the training dataset observation weights at each step as well as the final weight for each base model for aggregation.

In the next exercise we will dive into the details of AdaBoost!

# Adaptive Boosting
Let’s take a deeper look at how AdaBoost works! AdaBoost can be used for both regression and classification, but in this example we will be solving a classification problem. We begin with the full Training Dataset. You will see that it consists of green circles and red triangles. The goal of our AdaBoost classifier will be to form a decision boundary that separates these two classes. Initially, the training data instances are all given the same weight. This is indicated by the size of shapes all being the same.

Our first step is to fit an estimator, the 1st Base Model. While boosting can be applied to any base machine learning model, we will use decision trees. But aren’t decision trees prone to overfitting? We already said that the base models for boosting are supposed to be very simple and tend to underfit. That is correct, and for this reason we use the simplest version of a decision tree, known as a decision stump. A decision stump only makes a single decision, so the resultant estimator only has two leaf nodes.

Taking a look at the Result of the 1st Base Model, we see that the decision boundary, that is the border between the lighter green and lighter red regions, does a decent job of separating the green circles from the red triangles. However we do notice that there are two red triangles in the light green region. This indicates that they have been classified incorrectly by the decision stump.

Each of the base models will contribute a different amount to the final ensemble model. The influence that a particular base model contributes is going to be dependent on the number of errors it makes, or for regression, the magnitude of the errors it makes. We do not want a decision stump that does a terrible job of classifying the data to have the same say as a decision stump that does a great job. Once we are able to evaluate the Result of the 1st Base Model, we can Weight the Model and assign it a value, here indicated by alpha_1.

To prepare for the next stage of the sequential learning process, we need to Reweight the Data. The instances of the training data that were classified incorrectly by the 1st Base Model, the two red triangles in the middle right, are given a larger weight than the other data instances indicated by their larger size. By assigning those misclassified points a larger weight, we are asking the the 2nd Base Model to give them preferential treatment during the Model Fitting.

Taking a look at the Result of the 2nd Base Model, we see that is exactly what happens. The two larger red triangles are classified correctly by the 2nd Base Model. Once again we assign the base model a weight, alpha_2 proportional to the errors it makes and prepare for the next stage of the sequential learning by reweighting the training data. The instances that were incorrectly classified by the 2nd Base Model, the two green circles in on the center right, are given a larger weight.

Once we have reached the predefined number of estimators for our AdaBoost model, the base models are ready to aggregate. In this example we have chosen n_estimators = 3. The influence of each base model in the final ensemble model will be proportional to the alpha it was assigned during the training process.

# Gradient Boosting Overview
Gradient Boosting is a sequential ensembling method that can be used for both classification and regression. It can use any base machine learning model, though it is most commonly used with decision trees, known as Gradient Boosted Trees.

For Gradient Boost, the Sequential Fitting Method is accomplished by fitting a base model to the negative gradient of the error in the previous stage. The Aggregation Method is a weighted sum of those base models where the model weight is constant.

The training of a Gradient Boosted model is the process of determining the base model error at each step and using those to determine how to best formulate the subsequent base model.

In the next exercise we will dive into the details of Gradient Boosting!

# Gradient Boosting
Now we will take a deeper look at how Gradient Boosting works. While Gradient Boosting can be applied to any base machine learning model, decision trees are commonly used in practice. In this example we will be focusing on a Gradient Boosted Trees model.

Our first step is to fit an estimator, the 1st Base Model. Recall that the base estimators for boosting algorithms tend to be simple and high bias. In contrast to AdaBoost which leveraged the simplest form of decision trees, the decision stump with only 1 level, gradient boosted trees can and actually do tend to include a few more decision branches. Often gradient boosted trees will have up to 32 leaf nodes, which corresponds to a tree depth of 5 levels. In this example, we are limiting the depth of the base estimators to 2, corresponding to 4 leaf nodes.

Once the 1st Base Model is trained, the residual errors (h_1), of the model given the training training data are determined. The residual error is the difference between the actual and predicted values for each of the training data instances.

h1=y(actual)−y(predicted)
 
The errors will be greater for the training data instances where the model did not do as good of a job with its prediction and will be lower on training data instances where the model fit the data well.

In the next stage of the sequential learning process, we fit the 2nd Base Model. Here is where the interesting part comes in. Instead of fitting the model to the target values y_actual as we are typically used to doing in machine learning, we actually fit the model on the errors of the previous stage, in this case h_1. The 2nd Base Model is literally learning from the mistakes of the 1st Base Model through those residuals that were calculated.

The results of the 2nd Base Model are multiplied by a constant learning rate, alpha, and added to the results of the 1st Base Model to give the set of updated predictions, The results of the second base model, which was tasked with fitting the errors of the first base model are multiplied by a constant learning rate, alpha and added to the results of the first base model to give us a set of updated predictions, y_2(predicted).

The residual errors of the 2nd stage are calculated using the updated predictions to get,

2(predicted)
h2=y(actual)−y2(predicted)
​
 
The subsequent stages repeat the same steps. At stage N, the base model is fit on the errors calculated at the previous stage h_(N-1). The new model that is fit is multiplied by the constant learning rate alpha and added to the predictions of the previous stage.

Once we have reached the predefined number of estimators for our Gradient Boosting model or the residual errors are not changing between iterations, the model will stop training and we end up with the resultant ensemble model.