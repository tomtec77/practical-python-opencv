import numpy as np
import argparse
import cv2

# Parse the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image, then split it into R, G, B channels
# Remember that OpenCV stored RGB images as NumPy arrays in reverse
# channel order
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# Merge the channels back together with the cv2.merge function
# With the following code we can show the actual colour of the channel
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)


