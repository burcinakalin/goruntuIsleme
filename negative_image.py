import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread('/home/burcin/Desktop/agac.jpg')
%matplotlib inline

print(255-img[84,98])
img_neg = np.zeros(img.shape, type(img[0,0,0]))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_neg[i,j] =  1 - img[i,j]
plt.subplot(1,2,1), plt.imshow(img)
plt.subplot(1,2,2), plt.imshow(img_neg)

plt.show()
