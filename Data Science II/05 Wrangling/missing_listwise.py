import pandas as pd
import numpy as np

d = {'Date': ['01-Sept','02-Sept','03-Sept','04-Sept','05-Sept',
            '06-Sept','07-Sept','08-Sept','09-Sept','10-Sept'], 
    'Temperature': [18,17,14,16,15,14,16,19,13,14],
    'WindSpeed': [9,12,np.nan,6,np.nan,10,13,np.nan,18,5],
    'Rainfall': [1,3,np.nan,0,np.nan,4,5,np.nan,7,6]}

df = pd.DataFrame(data=d)

# TO DO
df.dropna(inplace=True) 
print(df.head(10))