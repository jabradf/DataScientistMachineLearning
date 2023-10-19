import numpy as np
cm = ([25, 25], [5,4])

true_pos = 25
true_neg = 36
false_pos = 5
false_neg = 4

precision = np.sum(true_pos / (true_pos + false_pos))
recall = np.sum(true_pos / (true_pos + false_neg))

print("precision", precision)
print("recall", recall)