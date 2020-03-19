#Inserting a new column into a existing data
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(exam_data,labels)
print(df)
df['age']=[21,20,19,21,25,24,23,18,24,26]
print(df)

df2=df.assign(status=['Pass','Pass','Fail','Pass','Fail','Pass','fail','Pass','Fail','Pass'],index=3)
print(df2)
