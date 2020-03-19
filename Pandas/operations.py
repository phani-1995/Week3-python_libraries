#program to add, subtract, multiple and divide two Pandas Series.

import pandas as pd
df=pd.Series([2,4,6,8,10])
print(df)
df1=pd.Series([1,3,5,7,9])
print(df1)
#Adding two series
df2=df+df1
print("The addition of two series is : ",df2)
#Subtract from two series
df3=df-df1
print("The subtraction of two series is: ",df3)
#Multiply the two series
df4=df * df1
print("The multiplication of two series: ",df4)
#Division of two series
df5=df/df1
print("The division of two series is: ",df5)

