import cv2
import matplotlib.pyplot as pp
import numpy as np


def ROI(img, vertices):
    mask = np.zeros_like(img)  # create black image of size of image
    match_mask_color = 255  # as its a gray_ scale image we dnt need (255,) * channel
    cv2.fillPoly(mask, vertices, match_mask_color)  # set vertices which from poly which match_mask_color
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_line_image(img, lines):
    blank_image = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)  # create blank image with
    # same dimension for original
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
    draw_line = cv2.addWeighted(img, 0.8, blank_image, 20, 0)
    # draw_line = cv2.bitwise_xor(img, blank_image)
    return draw_line


image = cv2.imread('Road.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)  # because matplotlib takes RGB

# We have to create ROI
print(image.shape)
height = image.shape[0]
width = image.shape[1]
Region_Interested_vertices = [(0, height), (width / 2, height / 2), (width, height)]

# to detect edge we need gray_scaled image
gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
Canny_edge = cv2.Canny(gray_scale, 50, 100)

Cropped_image = ROI(Canny_edge, np.array([Region_Interested_vertices], np.int32))
lines = cv2.HoughLinesP(Cropped_image,
                        rho=6,
                        theta=np.pi / 180,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=10)
image_with_line = draw_line_image(image, lines)
pp.imshow(image_with_line)
pp.show()
