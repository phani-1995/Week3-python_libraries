#Python program to remove specific elements in a numpy array.
import numpy as np
arr=np.array([10,20,30,40,50,60,70,80,90,100])
print("The original array is: ")
print(arr)
print(np.delete(arr,[0,3,4]))   