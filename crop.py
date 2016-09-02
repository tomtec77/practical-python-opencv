import numpy as np
import argparse
import cv2

# Parse the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load and display the original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Crop the image
# Supply NumPy array slices to extract a rectangular section of the image
# starting at (130,150) and ending at (420,310) - height first, width
# second
cropped = image[150:310, 130:420]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)

