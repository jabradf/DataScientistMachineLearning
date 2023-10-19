'''
We’ve imported several DataFrames related to some of baseball’s biggest stars. We have data on Aaron Judge 
(http://m.mlb.com/player/592450/aaron-judge)
and Jose Altuve (http://m.mlb.com/player/514888/jose-altuve). Judge is one of the tallest players 
in the league and Altuve is one of the shortest. Their strike zones should be pretty different!

Each row in these DataFrames corresponds to a single pitch that the batter saw in the 2017 season. 
To begin, let’s take a look at all of the features of a pitch. Print aaron_judge.columns.

In this project, we’ll ask you to print out a lot of information. To avoid clutter, feel free to 
delete the print statements once you understand the data.

We used the pybaseball (https://github.com/jldbc/pybaseball) Python package to get the data for this project. 
If you’re interested in getting more data, the documentation for pybaseball can help you get data that 
you’re interested onto your own computer.
'''

#import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()

aaron_judge['type'] = aaron_judge['type'].map({'S': 1, 'B': 0})
#print(aaron_judge['plate_z'])
aaron_judge = aaron_judge.dropna(subset = ['type', 'plate_x', 'plate_z'])
print(aaron_judge.type)

training_set, training_labels = train_test_split(aaron_judge, random_state=1)
classifier = SVC(kernel='rbf', gamma = 3, C=1)
data = training_set[['plate_x','plate_z']]
classifier.fit(data, training_set['type'])

plt.scatter(x=aaron_judge['plate_x'], y=aaron_judge['plate_z'], c=aaron_judge['type'], cmap = plt.cm.coolwarm, alpha=0.25)
draw_boundary(ax, classifier)
plt.show()

score = classifier.score(data, training_set['type'])
print("score: ", score)