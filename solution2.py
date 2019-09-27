import os
import matplotlib.pyplot as plt 
import numpy as np 
import math

def gfilter(img, w, std):
    kernel = np.random.normal(0, std, (w, w))
    kernel = np.fabs(kernel)
    kernel/= kernel.sum()

    shape_0 = img.shape[0]
    shape_1 = img.shape[1]  

    img2 = np.zeros_like(img)

    r = w // 2

    for c in range(3):
        for i in range(r, shape_0 - r):
            for j in range(r, shape_1 - r):
                s = kernel*img[i - r : i + r + 1, j - r: j + r + 1, c]
                img2[i, j, c] = s.sum()
    return img2     

def gfilter_1(img, w, std):
    kernel = np.random.normal(0, std, w)
    kernel = np.fabs(kernel)
    kernel/= kernel.sum()

    shape_0 = img.shape[0]
    shape_1 = img.shape[1]  

    img2 = np.zeros_like(img)

    r = w // 2

    for i in range(r, shape_0 - r):
        for j in range(r, shape_1 - r):
            for c in range(3):
                s = kernel*img[i, j - r : j + r + 1, c]
                img2[i, j, c] = s.sum()
    
    img3 = np.zeros_like(img2)

    kernel = np.random.normal(0, std, w)
    kernel = np.fabs(kernel)
    kernel/= kernel.sum()

    for i in range(r, shape_0 - r):
        for j in range(r, shape_1 - r):
            for c in range(3):
                s = kernel*img2[i - r : i + r + 1, j, c]
                img3[i, j, c] = s.sum()
    return img3

img = plt.imread('c:/Users/Alice/Documents/lena.png', 0)
fig, axs = plt.subplots(1,3)
img2 = gfilter(img, 3, 1)
img3 = gfilter_1(img, 3, 1)
axs[0].imshow(img2)
axs[1].imshow(img3)
axs[2].imshow(img)
plt.show()