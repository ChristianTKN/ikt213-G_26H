import cv2

image = cv2.imread("pictures/lambo.png")

def sobel_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    sobel = cv2.Sobel(blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1)

    return sobel
print_out = sobel_edge_detection(image)

cv2.imwrite("pictures/sobel_edge_detection.png", print_out)
