import cv2
import matplotlib.pyplot as pp
import numpy as np


def ROI(frame, vertices):
    mask = np.zeros_like(frame)
    match_mask_colour = 255  # white color
    cv2.fillPoly(mask, vertices, match_mask_colour)
    cv2.imshow('mask', mask)
    masked_frame = cv2.bitwise_and(frame, mask)
    return masked_frame


def draw_line_frames(frame, lines):
    blank_frame = np.zeros((frame.shape[0], frame.shape[1], frame.shape[2]), np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_frame, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)

    frame_wit_draw_line = cv2.addWeighted(frame, 0.8, blank_frame, 20, 0)
    return frame_wit_draw_line


cap = cv2.VideoCapture('test2.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read( )
while ret:

    height = frame1.shape[0]
    width = frame1.shape[1]
    region_interested = [(0, height), (width / 2, height / 2), (width, height)]

    gray_scaled_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame_edges = cv2.Canny(frame1, 50, 100)

    cropped_frame = ROI(frame_edges, np.array([region_interested], np.int32))
    lines = cv2.HoughLinesP(cropped_frame,
                            rho=4,
                            theta=np.pi / 180,
                            threshold=160,
                            minLineLength=40,
                            maxLineGap=25,
                            lines=None
                            )
    frame_with_line = draw_line_frames(frame1, lines)
    cv2.imshow('Video', frame_with_line)
    k = cv2.waitKey(1)
    frame1 = frame2
    _, frame2 = cap.read()
    k = cv2.waitKey(1)
    if k == 27:
        ret = False
cap.release()
cv2.destroyAllWindows()
