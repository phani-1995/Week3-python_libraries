import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("medal.csv",sep=",")
print(data)
country=data['country']
goldMedal=data['gold_medal']
plt.pie(goldMedal,labels=country, autopct="%1.1f%%")
plt.show()