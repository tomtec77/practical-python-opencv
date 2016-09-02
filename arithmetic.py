from __future__ import print_function
import numpy as np
import argparse
import cv2

# Parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load and display the original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# OpenCV addition: values are clipped to ensure they never fall outside
# the range [0,255]
print("Max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("Min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

# NumPy addition: values wrap around (modulo arithmetic)
print("Wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("Wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

# Now perform arithmetic on actual images
# Add 100 to every pixel on the image; the result will look more "washed
# out" than the original
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

# Subtract 50 from every pixel; the result looks darker than the original
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)


