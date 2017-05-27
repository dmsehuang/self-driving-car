import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read image and copy image
img = mpimg.imread('test.jpg')
region_select = np.copy(img)

xsize = img.shape[1]
ysize = img.shape[0]

# Define a triangle. In production, this should be a polynomial
bottom_left = [0, ysize]
bottom_right = [xsize, ysize]
apex = [xsize/2.0, ysize/1.68]

# Draw boundries
# 1. Get coefficients
left_fit = np.polyfit([bottom_left[0], apex[0]], [bottom_left[1], apex[1]], 1)
right_fit = np.polyfit([bottom_right[0], apex[0]],[bottom_right[1], apex[1]], 1)
bottom_fit = np.polyfit([bottom_left[0], bottom_right[0]], \
                        [bottom_left[1], bottom_right[1]], 1)
# 2. Draw lines
left_line = np.poly1d(left_fit)
right_line = np.poly1d(right_fit)
bottom_line = np.poly1d(bottom_fit)

# Find region
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
idx = (YY > left_line(XX)) & \
        (YY > right_line(XX)) & \
        (YY < bottom_line(XX))

# Mark the region as red
region_select[idx] = [255, 0 , 0]

# Save image
mpimg.imsave('region_select.jpg', region_select)
