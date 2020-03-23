import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=np.array([[2,4,6,8,10],[4,2,4,2,2],[8,3,7,6,4],[5,4,4,4,3],[6,6,8,6,2]])
dataFrame=pd.DataFrame(data,columns=['a','b','c','d','e'], index=["Delhi",'Mumbai','Hyderabad','Pune','Bengalur'])
dataFrame.plot(kind='bar')
plt.show()