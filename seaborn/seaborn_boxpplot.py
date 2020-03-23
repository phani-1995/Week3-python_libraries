import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
data=pd.read_csv("https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv")
print(data)
sb.boxplot(x='lifeExp', y='continent', data=data)
plt.show()