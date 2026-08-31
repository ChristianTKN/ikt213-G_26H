import cv2

image = cv2.imread("pictures/iris-1.png")

def padding(image, border_width):
    padded_image = cv2.copyMakeBorder(image,
                                      border_width,
                                      border_width,
                                      border_width,
                                      border_width,
                                      cv2.BORDER_REFLECT)
    return padded_image

result = padding(image, 100)
cv2.imwrite("pictures/iris_fixed_border.png", result)