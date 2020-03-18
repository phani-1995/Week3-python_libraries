#   
import numpy as np
x=np.ones((5,5),dtype=float)
print("The original array is: ")
print(x)
print("The array 1 on border 0 inside is: ")
x[1:-1,1:-1]=0
print(x)
