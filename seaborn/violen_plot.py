
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
print(data)

sb.violinplot(x='sex',y='total_bill', data=data)
plt.show()