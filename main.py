import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture("leopard.mp4")

framecount = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv.CAP_PROP_FPS)
while True:
    ret, frame = cap.read()
    time.sleep(1/fps)
    bw_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Frame", bw_frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
cap.release()