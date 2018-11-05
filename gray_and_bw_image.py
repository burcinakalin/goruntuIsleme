import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mgimg

def get_distance(v, w=[1/3,1/3,1/3]):
    a,b,c = v[0], v[1], v[2]
    w1,w2,w3 = w[0], w[1], w[2]
    d = ((a**2)*w1 +
         (b**2)*w2 +
         (c**2)*w3) **.5
    return d

def convert_rgb_to_gray(img):
    img2 = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img2[i,j] = get_distance(img[i,j,:])
    return img2

def convert_gray_level_to_BW(image_gray_level):
        m = image_gray_level.shape[0]
        n = image_gray_level.shape[1]
        image = np.zeros((m,n))
        for i in range(m):
            for j in range(n):
                if image_gray_level[i,j]>120:
                    image[i,j] = 1
                else:
                    image[i,j] = 0
        return image

img=mpimg.imread('/home/burcin/Desktop/agac.jpg')
img2 = convert_rgb_to_gray(img)
img3 = convert_gray_level_to_BW(img2)
%matplotlib inline

plt.subplot(1,3,1),plt.imshow(img)
plt.subplot(1,3,2),plt.imshow(img2,cmap='gray')
plt.subplot(1,3,3),plt.imshow(img3,cmap='gray')

