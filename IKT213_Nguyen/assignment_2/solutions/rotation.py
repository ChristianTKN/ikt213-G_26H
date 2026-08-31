import cv2

image = cv2.imread("pictures/iris-1.png")

def rotation(image, rotation_angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image

angle = float(input("Enter the angle in degrees: "))
print_out = rotation(image, angle)

cv2.imwrite("pictures/rotated.png", print_out)