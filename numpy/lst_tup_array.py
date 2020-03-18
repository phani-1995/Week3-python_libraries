import numpy as np
try:
    list=[1,2,3,4,5,6,7,8]
    x=np.asarray(list)
    print("The coverted list to array is ",x)
    tuple=((8,4,6),(1,2,3))
    y=np.asarray(tuple)
    print("The converted list to tuple is ",y)
except:
    print("syntax Error")
