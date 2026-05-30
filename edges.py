import cv2
2

3
# Read the original image
4
img = cv2.imread('lena.jpg')
5
# Display original image
6
cv2.imshow('Original', img)
7
cv2.waitKey(0)
8

9
# Convert to graycsale
10
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
11
# Blur the image for better edge detection
12
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
13

14
# Sobel Edge Detection
15 
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
16
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
17
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
18
# Display Sobel Edge Detection Images
19 
cv2.imshow('Sobel X', sobelx)
20
cv2.waitKey(0)
21
cv2.imshow('Sobel Y', sobely)
22
cv2.waitKey(0)
23
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
2
cv2.waitKey(0)
25

26
# Canny Edge Detection
27
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
28
# Display Canny Edge Detection Image
29
cv2.imshow('Canny Edge Detection', edges)
30
cv2.waitKey(0)
31

32
cv2.destroyAllWindows()
