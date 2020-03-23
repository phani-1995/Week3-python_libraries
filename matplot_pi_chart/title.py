import matplotlib.pyplot as plt

lang=['java','Python','php','javaScript','c#','C++']
Popularity=[22.2,17.6,8.8,8,7.7,6.7]

plt.pie(Popularity,explode=(0.1,0,0,0,0,0),labels=lang,autopct='%1.1f%%')
plt.title("The Popularity of Programming Language ")
plt.show()