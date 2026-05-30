import cv2
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as pplot

img = cv2.imread('lena.jpg')
img_unchange = cv2.imread('alphaImage.png', cv2.IMREAD_UNCHANGED);
imga2 = cv2.imread('harryPotter.jpg', -1)
#displays the value of the pixe in BGR
#if image has alpha channel, 4 values will be displayed
print ("RGB values of pixel [20][20] in lena.jpg image")
print (img[20][20]) 

imga2Gray = cv2.cvtColor(imga2, cv2.COLOR_BGR2GRAY)

print ("Image Properties of Lena")
#print ("- Image format: " + str(img.format))
print ("- Image size: " + str(img.size))
print ("- Shape/Dimensions: " + str(img.shape))

cv2.namedWindow('lena image', cv2.WINDOW_NORMAL)
cv2.imshow('lena image', img)
cv2.namedWindow('dice image', cv2.WINDOW_NORMAL)
cv2.imshow('dice image', img_unchange)
cv2.namedWindow('HPotter image', cv2.WINDOW_NORMAL)
cv2.imshow('H Potter', imga2)
#blackWhite
#1) convert to gray scale
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('bw image', blackAndWhiteImage)
cv2.imshow('gray image', grayImage)

k = cv2.waitKey(0)
if k == 27:    #wait for ESC key
    cv2.destroyAllWindows()
elif k == ord('s'):   #wait for 's' key to save and exit
    img=cv2.imread('lena.jpg',0)
    pplot.imshow(img, cmap='gray', interpolation ='bicubic' )
    pplot.xticks([]), pplot.yticks([])  #hide tick values on x and y axis
    pplot.show()
    
 