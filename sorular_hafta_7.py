#a)28 x 28 boyutlarında içeriği 0 ve 1 olan bir matris üretiniz.
#b) a da üretilen matrisde 1 leri içeren MBR dikdörtgeni üreten fonk yaz.
#c)kendisine aktarılan iki vektörün, benzerliğini geri döndüren fonk.
#d) a şıkkında üretilen fonk kullanarak 100 farklı matris elde edip. 1. üretilen ile diğerlerini 
#karşılaştırıp benzerliğini listele

import random
import numpy as np

def matris_uret():
    matris=np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            matris[i,j] =random.randint(0,1)
    return matris

def MBR_create_28_by_28_with_0_1(matris_a):
    m = matris_a.shape[0]
    n = matris_a.shape[1]
    
    x_min=m
    x_max=0 #başlangıc degerleri olarak en olumsuz durum
    y_min=n
    y_max=0
    
    for i in range(m):
        for j in range(n):
            if(matris_a[i,j]==1 and x_min>i):
                x_min=i
                
            if(matris_a[i,j]==1 and x_max<i):
                x_max=i
                
            if(matris_a[i,j]==1 and y_min>j):
                y_min=j
                
            if(matris_a[i,j]==1 and y_max<j):
                y_max=j
    return(x_min,x_max,y_min,y_max)

m=matris_uret()
m
MBR_create_28_by_28_with_0_1(m)

def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    similarity=0
    for i in range(m):
        for j in range(n):
            similarity=similarity+character_a[i,j]*character_b[i,j]
    return similarity

c_1=matris_uret()
c_2=matris_uret()
get_similarity(c_1,c_2)

def get_similarity_for_100_character(kac_karakter):
    characters=[] #dizi tanımla
    for i in range(kac_karakter):
        new_char=matris_uret()
        characters.append(new_char)  #ekleme işlemi
    for i in range(kac_karakter):
        benzerlik=get_similarity(characters[0],characters[i])
        print (benzerlik)

get_similarity_for_100_character(10)
