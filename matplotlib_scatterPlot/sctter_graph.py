import matplotlib.pyplot as plt
import numpy as np
x=np.random.rand(200)
y=np.random.rand(200)
plt.scatter(x,y, color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.show()