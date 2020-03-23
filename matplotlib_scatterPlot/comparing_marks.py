import matplotlib.pyplot as plt
import pandas as pd

mathMarks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
scienceMarks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
markRange = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(markRange, mathMarks,label='Math Marks',color='b')
plt.scatter(markRange, scienceMarks, label='Science Marks',color='g')
plt.title('Scatter Plot')
plt.xlabel("Marks Range")
plt.ylabel('Marks Scored')
plt.legend()
plt.show()