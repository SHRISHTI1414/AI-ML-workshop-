import numpy as np
from PIL import Image 

img= Image.open('nyc.jpg')
img_array=np.array(img)

img.show()

print(img_array.shape)
print(img_array.dtype)
print(img_array[0,0])
print(img_array[0,0,1])
print(img_array[0,0,2])
