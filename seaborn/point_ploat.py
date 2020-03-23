import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


data=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

sb.pointplot(x='sex',y='survived',hue='class',data=data)
plt.show()