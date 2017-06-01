import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

# Read image and convert it to grayscale for further processing.
# COLOR_BGR2GRAY is DIFFERENT from COLOR_RGB2GRAY
image = mpimg.imread('exit-ramp.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
mpimg.imsave('gray_image.jpg', gray_image)

# Apply Gaussian filter to the image to smooth it.
# Kernal size must be an odd number. The larger it is, the wider the blur are it
# is. The larger the sigma it is, the smoothier the image will be.
kernal_size = 5
sigma = 0
blur_image = cv2.GaussianBlur(gray_image, (kernal_size, kernal_size), sigma)
mpimg.imsave('smooth_image.jpg', blur_image)

# Apply Canny edge detection filter to the image.
low_threshold = 60
high_threshold = 120
edge_image = cv2.Canny(blur_image, low_threshold, high_threshold)
mpimg.imsave('edge.jpg', edge_image)
