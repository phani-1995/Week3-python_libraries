import matplotlib.pyplot as plt
import random
import math

balls=25
x=[random.triangular() for i in range(balls)]
y=[random.gauss(0.5,0.25) for i in range(balls)]
colors=[random.randint(5,15)**2 for i in range(balls)]
areas=[math.pi*random.randint(5,15)**2 for i in range(balls)]
plt.figure()
plt.scatter(x,y,s=areas,c=colors,alpha=0.85)
plt.axis([0.0,1.0,0.,1.0])
plt.show()