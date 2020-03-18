import numpy as np
y=np.zeros((5,5),dtype=float)
print("The original matrix is: ")
print(y)
y[1:-1,1:-1]=1
print("The matrix is: ")
print(y)

