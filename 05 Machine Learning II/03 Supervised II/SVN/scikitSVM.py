from sklearn.svm import SVC
#from graph import points, labels

classifier = SVC(kernel = 'linear')

training_points = [[1, 2], [1, 5], [2, 2], [7, 5], [9, 4], [8, 2]]
labels = [1, 1, 1, 0, 0, 0]
#classifier.fit(points, labels) 
classifier.fit(training_points, labels) 

print(classifier.predict([[3, 4], [6,7]]))
#print(classifier.predict([[6, 7]]))

#classifier.support_vectors_