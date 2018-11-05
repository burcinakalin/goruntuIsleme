import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread("/home/burcin/Desktop/agac.jpg")
%matplotlib inline

def image_info(image):
    print("eksen sayısı : ",image.ndim)
    print("eksen değerleri : ",image.shape)

    print("en küçük kırmızı renk değeri : ",np.min(image[:,:,0]))
    print("en büyük kırmızı renk değeri : ",np.max(image[:,:,0]))

    print("en küçük yeşil renk değeri : ",np.min(image[:,:,1]))
    print("en büyük yeşil renk değeri : ",np.max(image[:,:,1]))

    print("en küçük mavi renk değeri : ",np.min(image[:,:,2]))
    print("en büyük mavi renk değeri : ",np.max(image[:,:,2]))
    plt.imshow(image)
    
image_info(img)
