import numpy as np
import argparse
import imutils
import cv2

# Parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load and display the original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Resize keeping the aspect ratio, which we calculate here
# We specify the width
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0]*r))

# Resizing of the image
# The interpolation parameter specifies which algorithm is actually used
# for the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width", resized)
cv2.waitKey(0)

# Resize specifying the height
r = 50.0 / image.shape[0]
dim = (int(image.shape[1]*r), 50)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# Instead of manually computing the aspect ratio and defining the
# dimensions, use the resize method provided by imutils
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via Function (Width)", resized)
cv2.waitKey(0)

# Resize via the height of the image
resized = imutils.resize(image, height=50)
cv2.imshow("Resized via Function (Height)", resized)
cv2.waitKey(0)
