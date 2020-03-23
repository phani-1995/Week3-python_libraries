import matplotlib.pyplot as plt
import numpy as np
men = (22, 30, 35, 35, 26)
women = (25, 32, 30, 35, 29)
group=5

fig,ax=plt.subplots()
index=np.arange(group)
bar_width=0.35
opacity=0.8
rects1=plt.bar(index,men,bar_width,alpha=opacity,color='green',label='Men')
rects2=plt.bar(index+bar_width,women,bar_width,alpha=opacity,color='orange',label="Women")
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by Person data')
plt.xticks(index+bar_width, ('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()