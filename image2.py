import cv2
import numpy as np
#has to be same size
# Read First Image
img1 = cv2.imread('lena.jpg')

# Read Second Image
img2 = cv2.imread('lena.jpg')
img3 = cv2.imread('harryPotter.jpg')

# concatanate image Horizontally
Hori = np.concatenate((img1, img2), axis=1)

# concatanate image Vertically
Verti = np.concatenate((img1, img2), axis=0)

cv2.imshow('HORIZONTAL', Hori)
cv2.imshow('VERTICAL', Verti)

cv2.waitKey(0)
cv2.destroyAllWindows()
