import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.head())
students.grade = students.grade.str.split('(\d+)', expand=True)[1]
#print(split_df.head())
students.grade = pd.to_numeric(students.grade)
print(students.dtypes)

print('mean:')
avg_grade = students.grade.mean()
print(avg_grade)