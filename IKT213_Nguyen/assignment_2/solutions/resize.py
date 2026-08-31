import cv2

image = cv2.imread("pictures/iris-1.png")

def resize_img(image, width, height):
    resized = cv2.resize(image, (width, height))
    return resized

printout = resize_img(image, 200, 200)
cv2.imwrite("pictures/resized.png", printout)