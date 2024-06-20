import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.head())

#method 1: drop them
#bill_df = bill_df.dropna()
#bill_df = bill_df.dropna(subset=['num_guests'])

#method 2: specify an aggregate number
#bill_df = bill_df.fillna(value={"bill":bill_df.bill.mean(), "num_guests":bill_df.num_guests.mean()})

score_mean = students.score.mean()
print(score_mean)

students = students.fillna(value=0)

score_mean_2 = students.score.mean()
print(score_mean_2)