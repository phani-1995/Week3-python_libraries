import matplotlib.pyplot as plt

lang=['Java', 'Python', 'PHP', 'JavaScript', 'C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
xPos=[i for i,_ in enumerate(lang)]
fig,ax=plt.subplots()

rects=ax.bar(xPos,popularity,color=('Blue','Green','Red','Yellow','cyan','Violet'))
plt.xlabel('programing Languages')
plt.ylabel('Popularity(%)')
plt.title('Programing Language bar representation')
plt.xticks(xPos,lang)
plt.minorticks_on()
for rec in rects:
    height=rec.get_height()
    ax.text(rec.get_x()+rec.get_width()/2., 1.05*height, '%f'%float(height),ha='center',va='bottom')
plt.show()