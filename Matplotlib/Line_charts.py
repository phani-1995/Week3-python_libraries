import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\p#an!\\Desktop\\WEEK 3\\Matplotlib\\fdata.csv",sep=",", parse_dates=True, index_col=0)
print(data.plot())
plt.show()