#Using different colors

import matplotlib.pyplot as plt

lang=['Java', 'Python', 'PHP', 'JavaScript', 'C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(lang,popularity,color=('Blue','Green','Red','Yellow','cyan','Violet'))
plt.xlabel('programing Languages')
plt.ylabel('Popularity(%)')
plt.title('Programing Language bar representation')
plt.show()