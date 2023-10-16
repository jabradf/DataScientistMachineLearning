#import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

breast_cancer_data = load_breast_cancer()

[training_data, validation_data, training_labels, validation_labels] = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size=0.2, random_state=100)

#print(len(training_data))
#print(len(training_labels))

bestK = 0
highestK = 0
accuracies = []
for kNum in range(1, 100, 2):
  classifier = KNeighborsClassifier(n_neighbors=kNum)
  classifier.fit(training_data, training_labels)
  result = classifier.score(validation_data, validation_labels)
  if result > highestK:
    bestK = kNum
    highestK = result
  #print(result)
  accuracies.append(result)


k_list = range(1,100,2)
print("best K: " + str(bestK))
print("highestK: " + str(highestK))
#print(len(accuracies))
plt.plot(k_list, accuracies)
plt.xlabel("Validation accuracy")
plt.title("Classifier accuracy")
plt.show()