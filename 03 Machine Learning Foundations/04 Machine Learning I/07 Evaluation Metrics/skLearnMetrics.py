'''Classifying a single point can result in a true positive (actual = 1, predicted = 1), a true negative 
(actual = 0, predicted = 0), a false positive (actual = 0, predicted = 1), or a false negative 
(actual = 1, predicted = 0). These values are often summarized in a confusion matrix.
Accuracy measures how many classifications your algorithm got correct out of every classification it made.
Recall is the ratio of correct positive predictions classifications made by the model to all actual positives.
Precision is the ratio of correct positive classifications to all positive classifications made by the model.
F1-score is a combination of precision and recall.
F1-score will be low if either precision or recall is low.'''

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]


print(accuracy_score(predicted, actual))
print(recall_score(predicted, actual))
print(precision_score(predicted, actual))
print(f1_score(predicted, actual))