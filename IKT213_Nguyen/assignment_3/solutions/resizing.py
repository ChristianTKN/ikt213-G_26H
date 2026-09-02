import cv2

image = cv2.imread("pictures/lambo.png")

def resize(image, scale_factor: int, up_or_down: str):
    resized_image = image

    if up_or_down == "up":
        for i in range(scale_factor):
            resized_image = cv2.pyrUp(resized_image)

    elif up_or_down == "down":
        for i in range(scale_factor):
            resized_image = cv2.pyrDown(resized_image)

    return resized_image

print_out = resize(image, 2, up_or_down="up")
cv2.imwrite("pictures/image_size_up.png", print_out)

print_out = resize(image, 2, up_or_down="down")
cv2.imwrite("pictures/image_size_down.png", print_out)