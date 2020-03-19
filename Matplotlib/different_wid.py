import matplotlib.pyplot as plt

x1=[1,2,3]
y1=[10,20,5]
x2=[1,2,3]
y2=[40,10,5]
plt.plot(x1,y1,color='blue',label='dotted',linestyle='dotted')
plt.plot(x2,y2,color='green',label='dashed',linestyle='dashed')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Two line Plot")
plt.show()