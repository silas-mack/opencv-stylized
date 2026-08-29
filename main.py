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
    pxl_size = 10
    temp_small = cv.resize(bw_frame, (int(frame.shape[1] / pxl_size), int(frame.shape[0] / pxl_size)), interpolation=cv.INTER_LINEAR)
    pxl_frame = cv.resize(temp_small, (frame.shape[1], frame.shape[0]), interpolation=cv.INTER_NEAREST)
    inv_frame = pxl_frame.copy()
    inv_frame[:,:] = 255-pxl_frame[:,:]
    #txt_frame = cv.putText(pxl_frame, "Test", (10,10), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv.imshow("Frame", inv_frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
cap.release()