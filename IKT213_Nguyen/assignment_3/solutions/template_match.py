import cv2
import numpy as np

image = cv2.imread("pictures/shapes-1.png")
template = cv2.imread("pictures/shapes_template.jpg")

def template_match(image, template):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    location = np.where(result >= threshold)

    height, width = gray_template.shape

    for point in zip(*location[::-1]):
        cv2.rectangle(image, point, (point[0] + width, point[1] + height), (0, 0, 255), 2)

    return image


print_out = template_match(image, template)

cv2.imwrite("pictures/template_match.png", print_out)

