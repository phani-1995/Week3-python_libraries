import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

programming_langs = ['C', 'C#','Java Script', 'Java', 'Python', 'PHP']
populatrity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

ax.bar(programming_langs,populatrity)
plt.show()