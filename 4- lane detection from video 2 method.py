import cv2
import numpy as np


def ROI(img, vertices):
    mask = np.zeros_like(img)  # create black frame of size of frame
    match_mask_color = 255  # as its a gray_ scale frame we dnt need (255,) * channel
    cv2.fillPoly(mask, vertices, match_mask_color)  # set vertices which from poly which match_mask_color
    masked_frame = cv2.bitwise_and(img, mask)
    return masked_frame


def draw_line_frame(img, lines):
    blank_frame = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)  # create blank frame with
    # same dimension for original
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_frame, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
    draw_line = cv2.addWeighted(img, 0.8, blank_frame, 20, 0)
    # draw_line = cv2.bitwise_xor(img, blank_frame)
    return draw_line


def process(frame):
    # We have to create ROI
    print(frame.shape)
    height = frame.shape[0]
    width = frame.shape[1]
    Region_Interested_vertices = [(0, height), (width / 2, height / 2), (width, height)]

    # to detect edge we need gray_scaled frame
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Canny_edge = cv2.Canny(gray_scale, 50, 100)

    Cropped_frame = ROI(Canny_edge, np.array([Region_Interested_vertices], np.int32))
    lines = cv2.HoughLinesP(Cropped_frame,
                            rho=6,
                            theta=np.pi / 180,
                            threshold=160,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=10)
    frame_with_line = draw_line_frame(frame, lines)
    return frame_with_line


cap = cv2.VideoCapture('test2.mp4')
while cap.isOpened():
    _, frame = cap.read()
    cv2.imshow('Video', process(frame))
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()