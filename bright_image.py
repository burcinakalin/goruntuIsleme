import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img_1=mpimg.imread('/home/burcin/Desktop/agac.jpg')
plt.imshow(img_1)
plt.show()

def parlaklik_azalt(img_1):
    for i in range(img_1.shape[0]):
        for j in range(img_1.shape[1]):
            n=(img_1[i,j,:])-50
            img2[i,j,:]=n
    return img2

plt.imshow(img_1)
plt.show()

img2 = parlaklik_azalt(img_1)

plt.imshow(img2)
plt.show()
