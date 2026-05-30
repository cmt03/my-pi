import cv2

im1 = cv2.imread("lena.jpg")
im2 = cv2.imread("lena.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow('lena.jpg',im2)

dimensions = im1.shape

height = im1.shape[0]
im1_size = im1.size
print("Image dimensions: " + str(dimensions) )
print("Image height:" + str (dimensions[0]) )
print("Image size: " + str(im1_size)) 

im3 = cv2.imread('harryPotter.jpg')
cv2.imshow('harrypotter.jpg',im3)
dPotter = im3.shape
height = im3.shape[0]
im3_size=im3.size
print("Image dimensions: " + str(dPotter) )
print("Image height:" + str (dPotter[0]) )
print("Image size: " + str(im3_size)) 

cv2.waitKey(0)
cv2.destroyAllWindows()