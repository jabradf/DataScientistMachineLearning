import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.columns)
students = pd.melt(frame=students, id_vars=["full_name", "gender_age", "grade"], value_vars=["fractions","probability"], var_name="exam", value_name="score")

print(students.head())
print(students.columns)
print(students.exam.value_counts())