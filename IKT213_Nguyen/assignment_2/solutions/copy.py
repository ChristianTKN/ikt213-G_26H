import cv2
import numpy as np

image = cv2.imread("pictures/iris-1.png")

def print_image_information(image):
    height, width, channels = image.shape
    return height, width, channels


def copy(image, emptyPictureArray):
    height, width, channels = image.shape

    for y in range(height):
        for x in range(width):
            emptyPictureArray[y, x] = image[y, x]

    return emptyPictureArray

height, width, channels = print_image_information(image)

emptyPictureArray = np.zeros((height, width, channels), dtype=np.uint8)

copied_image = copy(image, emptyPictureArray)
cv2.imwrite("pictures/copied_iris_image.png", copied_image)