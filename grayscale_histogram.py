from matplotlib import pyplot as plt
import argparse
import cv2

# Parse the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load an image and convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

# Compute the histogram
# 1st argument: the image to process (pass as a list)
# 2nd: indexes of the channels we want to compute a histogram for
# 3rd: you can supply a mask here to compute a histogram for masked
# pixels only
# 4th: number of bins (a list, one for each channel)
# 5th: specify the range of possible pixel values
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
