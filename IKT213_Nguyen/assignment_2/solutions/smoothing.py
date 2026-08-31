import cv2

image = cv2.imread("pictures/iris-1.png")

def smoothing(image):
    smoothed_image = cv2.GaussianBlur(image, (15, 15), 0, borderType=cv2.BORDER_DEFAULT)
    return smoothed_image

print_out=smoothing(image)

cv2.imwrite("pictures/smoothed_out.png", print_out)