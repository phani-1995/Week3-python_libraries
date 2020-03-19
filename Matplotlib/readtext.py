import matplotlib.pyplot as plt
with open("text.txt") as f:
    data=f.read()
data=data.split('\n')
x=[row.split(' ')[0] for row in data]
y=[row.split(' ')[1] for row in data]
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Graph ')
plt.show()

