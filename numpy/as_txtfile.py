import numpy as np
arr=np.arange(1,10,2)
print("The array is: ",arr)
y=np.savetxt("arrfile.txt",arr,delimiter=',')
z=open('arrfile.txt','r')
print(z.read())         