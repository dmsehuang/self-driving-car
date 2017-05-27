# Import required libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Loop through a set of threshold.
# Read image and copying it to a new matrix.
img = mpimg.imread('test.jpg')

arr = np.arange(160, 250, 5)

for i in arr:
    # Get the dimension of the image
    ysize = img.shape[0]
    xsize = img.shape[1]
    color_select = np.copy(img)

    # Set up threshold.
    r_threshold = i
    g_threshold = i
    b_threshold = i

    # Manipulate the image.
    idx = (img[:,:,0] < r_threshold) \
            | (img[:,:,1] < g_threshold) \
            | (img[:,:,2] < b_threshold)
    color_select[idx] = [0,0,0]

    # show the image
    plt.imshow(color_select)

    # Save image.
    name = "test-after" + str(i) + ".jpg"
    mpimg.imsave(name, color_select)
