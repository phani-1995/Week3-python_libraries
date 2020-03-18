import numpy as np
x=np.array([[0,1,3],[5,7,9]])
y=np.array([[0,2,4],[6,8,10]])
z=np.concatenate((x,y),1)
print("The matrix obtained is: ")
print(z)
