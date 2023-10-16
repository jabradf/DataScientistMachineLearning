actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(predicted)):
  #True Positives
  if actual[i] == 1 and predicted[i] == 1:
    true_positives += 1
  #True Negatives
  if actual[i] == 0 and predicted[i] == 0:
    true_negatives += 1 
  #False Positives
  if actual[i] == 0 and predicted[i] == 1:
    false_positives += 1
  #False Negatives
  if actual[i] == 1 and predicted[i] == 0:
    false_negatives += 1
  
accuracy = (true_positives + true_negatives) / (true_positives + true_negatives + false_positives + false_negatives)
print("Accuracy:", accuracy)