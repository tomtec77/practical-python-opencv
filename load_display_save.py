import argparse
import cv2

# Parse the command line arguments
# The only argument we need is the path to the image on disk
# Arguments are parsed and stored in a dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image from disk
# cv2.imread returns a NumPy array representing the image
image = cv2.imread(args["image"])
print "Width: %d pixels" % (image.shape[1])
print "Height: %d pixels" % (image.shape[0])
print "Channels: %d" % (image.shape[2])

# Display the actual image on screen, then pause the execution until any
# key is pressed
cv2.imshow("Image", image)
cv2.waitKey(0)

# Write the image to file in PNG format
# Conversion is automatic, based on file extension
cv2.imwrite("newimage.png", image)