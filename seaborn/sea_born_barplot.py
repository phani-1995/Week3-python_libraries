import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt
data1=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
print(data1)
sbs.barplot(x='sex',y='survived',hue="class",data=data1)
plt.show()
print(sep="   ")
sbs.barplot(x='sex',y='survived',hue='class',data=data)
plt.show()