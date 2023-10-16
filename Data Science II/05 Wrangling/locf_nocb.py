import pandas as pd
import numpy as np

d = {'timestamp': ['2021-11-11 12:00:00','2021-11-11 12:01:00','2021-11-11 12:02:00','2021-11-11 12:03:00','2021-11-11 12:04:00',
                    '2021-11-11 12:05:00','2021-11-11 12:06:00','2021-11-11 12:07:00','2021-11-11 12:08:00','2021-11-11 12:09:00'],
    'value1': [1,1,2,3,4,4,4,np.nan,6,6],
    'value2': [10,10,9,7,np.nan,5,5,5,5,5]
    }

df = pd.DataFrame(data=d)

## Fill in the missing data in the value1 column
df['value1'].ffill(axis=0, inplace=True)
#This fixes the second column:
df['value2'].bfill(axis=0, inplace=True)

print(df)