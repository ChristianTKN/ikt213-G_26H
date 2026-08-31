import cv2

image = cv2.imread("pictures/iris-1.png")

def crop(image, x_0, x_1, y_0, y_1):
    cropped = image[y_0:y_1, x_0:x_1]
    return cropped

height, width = image.shape[:2]
print_out = crop(img, 200,width - 130, 200, height - 130)
cv2.imwrite("pictures/cropped_result.png", print_out)