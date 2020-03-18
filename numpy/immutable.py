import numpy as np
x=np.zeros(10)
print(x)
x.flags.writeable = False
print("Test the array is read only or not: ")
x[0] = 1
print(x)
