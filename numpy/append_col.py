import numpy as np
x=np.array([[10,20,30],[40,50,60]])
print("The original array is: ")
print(x)
y=np.array([[100],[200]],dtype=int)
print(np.append(x,y,axis=1))