import matplotlib.pyplot as plt
import random
x,y=[],[]
for i in range(10):
    X=random.randint(0,100)
    x.append(X)
    Y=random.randint(0,100)
    y.append(Y)
print(x,"\n",y)
plt.scatter(x,y,facecolor='None',edgecolors='b')
plt.show()
