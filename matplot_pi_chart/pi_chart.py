import matplotlib.pyplot as plt
lang=['java','Python','PHP','javaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
explode = (0.1, 0, 0, 0,0,0)
plt.pie(popularity,explode=explode,labels=lang,autopct='%1.1f%%',shadow=True,startangle=140)
plt.axis('equal')
plt.show()