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

# Construct a NumPy array filled with zeros, same size as the original
# image, then draw a white rectangle in the center
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
cv2.rectangle(mask, (cX-75, cY-75), (cX+75, cY+75), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

# The bitwise_and function is used to apply the mask to the image
# The AND function will be True for all pixels (same image in both
# arguments) - by supplying a mask the function only examines pixels that
# are on the mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Another example: circular mask
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

