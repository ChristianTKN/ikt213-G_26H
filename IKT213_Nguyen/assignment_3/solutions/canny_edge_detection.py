import cv2

image = cv2.imread("pictures/lambo.png")

def canny_edge_detection(image, threshold_1, threshold_2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blur, threshold_1, threshold_2)

    return edges

print_out = canny_edge_detection(image, 50, 50)

cv2.imwrite("pictures/canny_edge_detection.png", print_out)
