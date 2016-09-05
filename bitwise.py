import numpy as np
import cv2

# Initialise the image, then draw a white rectangle in the centre of it
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

# Initialise a second image, draw a circle in it
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

# Bitwise operations compare pixels from two images (except for the case
# of NOT, which work on just one image)
# Bitwise AND: true only when both pixels are > 0
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# Bitwise OR: true if either of the two pixels are > 0
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# Bitwise XOR: true if and only if either of the two pixels are > 0,
# but not both
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# Bitwise NOT: inverts the ON and OFF pixels in an image
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
