import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(data)
sb.violinplot(x='species',y='sepal_length',data=data)
plt.show()