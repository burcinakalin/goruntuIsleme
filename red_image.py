import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img_1=mpimg.imread('/home/burcin/Desktop/agac.jpg')
plt.imshow(img_1)
plt.show()

def convert_rgb_to_red(img_1):
    for i in range(img_1.shape[0]):
        for j in range(img_1.shape[1]):
            img_2[i,j,0] = img_1[i,j,0]+100
    return img_2
        
img2 = convert_rgb_to_red(img_1)
plt.imshow(img2),plt.show()
