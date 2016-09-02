import numpy as np
import argparse
import imutils
import cv2

# Parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load and display original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Determine the center of the image
# OpenCV allows you to specify any arbitrary point to rotate around,
# here we'll use the image center
(h, w) = image.shape[:2]
center = (w//2, h//2)

# Build the rotation matrix around the center, 45 degrees clockwise,
# without changing the scale
# cv2.warpAffine applies the transformation
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

# Rotate 90 degrees counterclockwise
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

# Instead of manually constructing M and calling the transformation, use
# the rotate function in imutils which does that for you
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

