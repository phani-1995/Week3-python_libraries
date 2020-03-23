
import matplotlib.pyplot as plt

lang=['Java', 'Python', 'PHP', 'JavaScript', 'C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]

yPos=[1,4,10,12,14,16]
plt.bar(yPos,popularity)
plt.xlabel('programing Languages')
plt.ylabel('Popularity(%)')
plt.title('Programing Language bar representation')
plt.show()