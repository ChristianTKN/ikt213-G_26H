import cv2
import numpy as np


image = cv2.imread("pictures/iris-1.png")
red, green, blue = cv2.split(image)

def print_image_information(image):
    height, width, channels = image.shape
    return height, width, channels

def hue_shifted(image, emptyPictureArray, hue):
    height, width, channels = image.shape

    for y in range(height):
        for x in range(width):
            for channel in range(channels):
                emptyPictureArray[y, x, channel] = (int(image[y, x, channel]) + hue) % 256

    return emptyPictureArray

height, width, channels = print_image_information(image)

emptyPictureArray_up = np.zeros((height, width, channels), dtype=np.uint8)

emptyPictureArray_down = np.zeros((height, width, channels), dtype=np.uint8)

print_out_value_up = hue_shifted(image, emptyPictureArray_up, 50)
print_out_value_down = hue_shifted(image, emptyPictureArray_down, -50)

cv2.imwrite("pictures/hue_shifted_up.png", print_out_value_up)
cv2.imwrite("pictures/hue_shifted_down.png", print_out_value_down)

"""
What happens if the color value is below 0 or exceeding 256?

If its exceed 256, the color value go back to 0 and still increas based of the value change

if its below 0, the color value will go back to the maximum value
"""