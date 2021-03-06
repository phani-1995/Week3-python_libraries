
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

men = (54.74,42.35,67.37,58.24,30.25)
menSTD=(4,3,4,1,5)
ind=np.arange(5)
width=0.35

fig, ax =plt.subplots()
rects1=ax.bar(ind,men,width,yerr=menSTD,color='g')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by Person data')

for rec in rects1:
    height=rec.get_height()
    ax.text(rec.get_x()+rec.get_width()/2.,1.05*height,"%d"%int(height),ha='center',va='bottom')
plt.show()