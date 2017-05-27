# Lane finding by combing color and region selection.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Loop through a set of threshold.
# Read image and copying it to a new matrix.
image = mpimg.imread('test.jpg')

# Get the dimension of the image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)
line_image = np.copy(image)

#  -----------------------------
# |         parameters          |
#  -----------------------------
# Set up threshold.
r_threshold = 200
g_threshold = 200
b_threshold = 200

# Define a triangle. In production, this should be a polynomial
left_bottom = [0, ysize]
right_bottom = [xsize, ysize]
apex = [xsize/2.0, ysize/1.642]

# ------------------------------------------
# |     step 1: find important area         |
# ------------------------------------------

# Draw boundries
# 1. Get coefficients
left_fit = np.polyfit([left_bottom[0], apex[0]], [left_bottom[1], apex[1]], 1)
right_fit = np.polyfit([right_bottom[0], apex[0]],[right_bottom[1], apex[1]], 1)
bottom_fit = np.polyfit([left_bottom[0], right_bottom[0]], \
                        [left_bottom[1], right_bottom[1]], 1)
# 2. Draw lines
left_line = np.poly1d(left_fit)
right_line = np.poly1d(right_fit)
bottom_line = np.poly1d(bottom_fit)

# Find region
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_thresholds = (YY > left_line(XX)) & \
                    (YY > right_line(XX)) & \
                    (YY < bottom_line(XX))

# ------------------------------------------------------
# |     step 2: find lane within important area         |
# ------------------------------------------------------
# Manipulate the image.
color_thresholds = (image[:,:,0] < r_threshold) \
                    | (image[:,:,1] < g_threshold) \
                    | (image[:,:,2] < b_threshold)

# manipulate image
black_out_idx = color_thresholds | ~region_thresholds
lane_idx = region_thresholds & ~color_thresholds
color_select[black_out_idx] = [0,0,0]
line_image[lane_idx] = [255, 0, 0]

# Save image.
mpimg.imsave("color-region.jpg", color_select)
mpimg.imsave("lane-highlight.jpg", line_image)
