import numpy as np
import argparse
import cv2

# Parse the command line argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load and display the original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Colour space conversions are specified by the cv2.COLOR_* flags
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# Convert to L*a*b
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b", lab)
cv2.waitKey(0)
