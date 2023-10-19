import pandas as pd


d = {'values': [['A','B','C','D'],['D','E','F'], ['A','D'], ['K']]}

df = pd.DataFrame(data=d)
df['id'] = df.index+1
print(df)

# ----------------------
# Method 1
df2 = df.explode('values')
df3 = pd.crosstab(df2['id'], df2['values']).replace({0: 'no_', 1: 'yes_'})

out = df.merge(df3.add(df3.columns), left_on='id', right_index=True)
print(df2)


'''print("---")
# Method 2
df2 = df['values'].agg('|'.join).str.get_dummies().replace({0: 'no_', 1: 'yes_'})
out = df.join(df2.add(df2.columns))
print(out)'''