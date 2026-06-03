import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the image (OpenCV loads as BGR)
img_bgr = cv2.imread("d:\python\image1\green.png")

# 2. Convert from BGR to HSV
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# 3. Convert BGR to RGB just for displaying correctly in Matplotlib
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 4. Display the original and the HSV channels inline
fig, axs = plt.subplots(1, 4, figsize=(15, 5))
axs[0].imshow(img_rgb)
axs[0].set_title("Original RGB")

# Show individual HSV channels
axs[1].imshow(img_hsv[:, :, 0], cmap="hsv")  # Hue Channel
axs[1].set_title("Hue (H)")

axs[2].imshow(img_hsv[:, :, 1], cmap="Greys")  # Saturation Channel
axs[2].set_title("Saturation (S)")

axs[3].imshow(img_hsv[:, :, 2], cmap="gray")  # Value Channel
axs[3].set_title("Value (V)")

plt.show()
