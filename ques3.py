import numpy as np
arr1=np.array([2,3,4])
arr2=np.array([5,6,7])
arr3= arr1+arr2
print(arr3)
arr4=arr3>10
print(arr3[arr4])
arr5=arr3<10
print(arr3[arr5])
