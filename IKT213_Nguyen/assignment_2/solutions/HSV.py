import cv2

image = cv2.imread("pictures/iris-1.png")
def HSV(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv

print_out = HSV(image)
cv2.imwrite("pictures/hsv_iris.png", print_out)