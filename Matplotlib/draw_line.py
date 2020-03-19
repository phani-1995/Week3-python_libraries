#program to draw a line with suitable label in the x axis, y axis and a title
import matplotlib.pyplot as  plt
import numpy as np
x=np.linspace(0,10,100)
plt.plot(x, x, label='linear')
plt.title("Draw line")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
