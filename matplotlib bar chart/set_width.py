import matplotlib.pyplot as plt

lang=['Java', 'Python', 'PHP', 'JavaScript', 'C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
xPos = [i for i, _ in enumerate(lang)]
widtha=[1,0.2,0.8,0.6,2,0.3]
pos=[2,5,10,17,22,33]
plt.xticks(xPos,lang)
plt.bar(pos,popularity,width=widtha)
plt.xticks(pos,lang)
plt.xlabel('programing Languages')
plt.ylabel('Popularity(%)')
plt.title('Programing Language bar representation')
plt.show()