#Python program to convert panda module series to list
import pandas as pd
data=pd.Series([3,5,6,7,8,9])
print(list(data))
print(data.tolist())
print(type(data.tolist()))
