import cv2


def print_image_information(image):
    height, width, channels = image.shape

    print("height: ", height)
    print("width: ", width)
    print("channels: ", channels)
    print("size: ", image.size)
    print("data type: ", image.dtype)

image = cv2.imread("iris-1.jpg")

print_image_information(image)