import cv2
import numpy as np

lenaPath = r'D:\Python\image1\lena.jpg'
harryFile='harryPotter.jpg'

# Read First Image - lena
img1 = cv2.imread(lenaPath, cv2.IMREAD_UNCHANGED) #cv2.IMREAD_COLOR)
print ("height and width of Lena Image", img1.shape)
cv2.imshow('lena',img1)

cv2.waitKey(0)

# Read Second Image
img2=cv2.imread(harryFile,cv2.IMREAD_GRAYSCALE)
print ("height and width of HPotter image", img2.shape)
cv2.imshow('HPotter image',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
