# Python program to find the number of elements of an array, length of one array element
# in bytes and total bytes consumed by the elements.
import numpy as np
x=np.array([10,20,30],dtype=float)
print("size: ", x.size)
print("length of an array element: ",x.itemsize)
print("Total bytes consumed by elements of an array is : ",x.nbytes)
