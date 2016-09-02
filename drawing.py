import numpy as np
import cv2

# Initialise the image: 300 x 300 pixels, 3 channels
# using 8-bit unsigned integers
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Draw a diagonal line from the top left to the bottom right corner,
# 1 px thick (the default)
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a diagonal line from the bottom left to the top right corner,
# 3 px thick
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a green rectangle (border only, 1 px thick)
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a red rectangle (border only, 3 px thick)
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a blue filled rectangle
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Reset the canvas to draw circles, and find its centre
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1]/2, canvas.shape[0]/2)

# Draw a series of white unfilled concentric circles
white = (255, 255, 255)
for r in xrange(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw 25 circles of random size, colour and position
for i in xrange(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
