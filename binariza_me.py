import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('prueba1.jpg',0)
img = cv2.medianBlur(img,11)

ret,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,67,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,4)

titles = ['Original Image', 'Global Thresholding (v = 90)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    cv2.imwrite('C:\Users\Rafael\Documents\Servicio Social\Interfaz\imagen_'+str(i)+'.jpg',images[i])
plt.show()
