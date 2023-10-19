from sklearn.metrics import confusion_matrix

actual =    [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(predicted)):
  #print(predicted[i], actual[i])
  if actual[i]==1 and predicted[i]==1:
    true_positives += 1
  if actual[i]==0 and predicted[i]==0:
    true_negatives += 1
  if actual[i]==0 and predicted[i]==1:
    false_positives += 1
  if actual[i]==1 and predicted[i]==0:
    false_negatives += 1

print("TP:", true_positives)
print("TN:", true_negatives)
print("FP:", false_positives)
print("FN:", false_negatives)

conf_matrix = confusion_matrix(actual, predicted)
print(conf_matrix)