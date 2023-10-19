#import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from graph import points, labels, draw_points, draw_margin

classifier = SVC(kernel='linear', C = 0.6)
points.append([3,3])
labels.append(0)
points.append([4,4])
labels.append(1)
points.append([10,6])
labels.append(1)
classifier.fit(points, labels)

draw_points(points, labels)
draw_margin(classifier)

plt.show()
