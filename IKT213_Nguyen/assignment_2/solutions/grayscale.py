import cv2


image = cv2.imread("pictures/iris-1.png")

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

print_out = grayscale(image)
cv2.imwrite("pictures/grayscaled.png", print_out)