import numpy as np
try:
    array=np.array([0,10,20,40,60,80])
    print(array)
    array1=np.array([10,30,40,50,70,90])
    print(array1)
    array3=np.setxor1d(array,array1)
    print("The array obtained after exclusive or operation is: ",array3)
except:
    print("Syntax error")