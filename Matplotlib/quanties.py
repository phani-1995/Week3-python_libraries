import matplotlib.pyplot as plt

x1 = [2, 3, 5, 6, 8]
y1 = [1, 5, 10, 18, 20]

x2 = [1, 4, 6, 7, 9]
y2 = [2, 6, 11, 20, 22]

plt.axis([0, 10, 0, 30])
plt.plot(x1, y1,'b*', x2, y2, 'ro')
plt.show()