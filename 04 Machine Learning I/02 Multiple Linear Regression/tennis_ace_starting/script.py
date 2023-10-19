#import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')
print(df.head())
print(df.info())
#print(df.Player.value_counts())

# perform exploratory analysis here:

plt.scatter(df.BreakPointsOpportunities, df.Winnings, alpha=0.2)
plt.xlabel("BreakPointsOpportunities")
plt.ylabel("Winnings")
plt.show()

# find some correlations between columns:
# double fault vs losses
# BreakPointsOpportunities vs Winnings


## perform single feature linear regressions here:
features = df[['FirstServeReturnPointsWon']]
outcome = df[['Winnings']]
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)
                
model = LinearRegression()
model.fit(features_train, outcome_train)
score = model.score(features_test, outcome_test)
print("training score:", score)

prediction = model.predict(features_test)

plt.scatter(outcome_test,prediction, alpha=0.4)
plt.title("FirstServeReturnPointsWon vs Winnings prediction results")
plt.show()



#double fault vs losses
features = df[['DoubleFaults']]
outcome = df[['Losses']]
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)
                
model = LinearRegression()
model.fit(features_train, outcome_train)
score = model.score(features_test, outcome_test)
print("training score:", score)

prediction = model.predict(features_test)

plt.scatter(outcome_test,prediction, alpha=0.4)
plt.title("DoubleFaults vs Losses prediction results")
plt.show()



# BreakPointsOpportunities vs Winnings
features = df[['BreakPointsOpportunities']]
outcome = df[['Winnings']]
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)
                
model = LinearRegression()
model.fit(features_train, outcome_train)
score = model.score(features_test, outcome_test)
print("training score:", score)

prediction = model.predict(features_test)

plt.scatter(outcome_test,prediction, alpha=0.4)
plt.title("BreakPointsOpportunities vs Winnings prediction results")
plt.show()



## perform two feature linear regressions here:
x = df[['BreakPointsOpportunities', 'FirstServeReturnPointsWon']]
y = df[['Winnings']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)
mlr = LinearRegression()
mlr.fit(x_train, y_train)
print("multiple score:",mlr.score(x_test, y_test))

############
features = df[['FirstServe','FirstServePointsWon','FirstServeReturnPointsWon',
'SecondServePointsWon','SecondServeReturnPointsWon','Aces',
'BreakPointsConverted','BreakPointsFaced','BreakPointsOpportunities',
'BreakPointsSaved','DoubleFaults','ReturnGamesPlayed','ReturnGamesWon',
'ReturnPointsWon','ServiceGamesPlayed','ServiceGamesWon','TotalPointsWon',
'TotalServicePointsWon']]
outcome = df[['Winnings']]


x_train, x_test, y_train, y_test = train_test_split(features, outcome, train_size = 0.8, test_size = 0.2, random_state=6)
mlr = LinearRegression()
mlr.fit(x_train, y_train)
print("multiple score (more):",mlr.score(x_test, y_test))

















## perform multiple feature linear regressions here:
