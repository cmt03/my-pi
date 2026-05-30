#source: https://datacarpentry.org/image-processing/05-creating-histograms/

import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt
#matplotlib widget

# read the image of a plant seedling as grayscale from the outset
image = skimage.io.imread(fname='lena.jpg', as_gray=True)

# display the image
fig, ax = plt.subplots()
plt.imshow(image, cmap='gray')
plt.show()