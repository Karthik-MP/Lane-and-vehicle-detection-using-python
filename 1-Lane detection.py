# Here we are define ROI region of interest
# in matplotlib x axis value changes normally where in y axis values change from top to bottom reverse from normal
import cv2
import matplotlib.pyplot as pp
import numpy as np

image = cv2.imread('Road.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)  # because matplotlib takes RGB

# We have to create ROI
print(image.shape)
height = image.shape[0]
width = image.shape[1]
Region_Interested_vertices = [(0, height), (width / 2, height / 2), (width, height)]


def ROI(img, vertices):
    mask = np.zeros_like(img)   # create black image of size of image
    channel_count = img.shape[2]    # check number of channels
    match_mask_color = (255,) * channel_count   # set all channel to 255 that is white colour
    cv2.fillPoly(mask, vertices, match_mask_color)  # set vertices which from poly which match_mask_color
    cv2.imshow('mask', mask)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


Cropped_image = ROI(image, np.array([Region_Interested_vertices], np.int32))
pp.imshow(Cropped_image)
pp.show()
