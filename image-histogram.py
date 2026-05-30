#histograms
# read original image, in full color
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('lena.jpg')

# display the image
cv2.imshow('lena image', image)

fig, ax = plt.subplots()
plt.imshow(image)
plt.show()

colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.figure()
plt.xlim([0, 256])
for channel_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(
        image[:, :, channel_id], bins=256, range=(0, 256)
    )
    plt.plot(bin_edges[0:-1], histogram, color=c)

plt.title("Color Histogram")
plt.xlabel("Color value")
plt.ylabel("Pixel count")

plt.show()