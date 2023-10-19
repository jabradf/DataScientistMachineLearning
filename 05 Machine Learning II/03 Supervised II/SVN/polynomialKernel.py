from sklearn.datasets import make_circles
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#Makes concentric circles
points, labels = make_circles(n_samples=300, factor=.2, noise=.05, random_state = 1)

#Makes training set and validation set.
training_data, validation_data, training_labels, validation_labels = train_test_split(points, labels, train_size = 0.8, test_size = 0.2, random_state = 100)

classifier = SVC(kernel = "linear", random_state = 1)
classifier.fit(training_data, training_labels)
#print(classifier.score(validation_data, validation_labels))

#print(training_data[0])

new_training = []
new_validation = []

for point in training_data:
  one = 2**0.5 * point[0] * point[1]
  two = point[0]**2
  three = point[1]**2
  new_training.append([one, two, three])

for point in validation_data:
  one = 2**0.5 * point[0] * point[1]
  two = point[0]**2
  three = point[1]**2
  new_validation.append([one, two, three])

classifier.fit(new_training, training_labels)
score = classifier.score(new_validation, validation_labels)
print(score)