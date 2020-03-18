import numpy as np
array=np.zeros((4,3))
array[3:,:3]=1
array[2:,:2]=1
array[1:,:1]=1
print(array)
