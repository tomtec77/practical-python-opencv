from __future__ import print_function
import argparse
import cv2

# Parse the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and display it on screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# OpenCV represents images as NumPy arrays.
# In order to access a pixel value, we just need to supply the x and y
# coordinates - from there, we're given a tuple representing the Blue,
# Green and Red colours (OpenCV stores RGB colours in reverse order)
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# We now manipulate the top left pixel of the image, setting it to red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# We can also use NumPy's array slicing capabilities to manipulate larger
# portions of the image
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
