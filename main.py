import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture("leopard.mp4")

frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*"MP4V")
out = cv.VideoWriter("output.mp4", fourcc, 24.0, (frame_width, frame_height))



while True:
    ret, frame = cap.read()
    # if not ret:
    #     cap.release()
    #     cap = cv.VideoCapture("leopard.mp4")
    #     ret, frame = cap.read()

    bw_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    pxl_size = 7
    temp_small = cv.resize(bw_frame, (int(frame.shape[1] / pxl_size), int(frame.shape[0] / pxl_size)), interpolation=cv.INTER_LINEAR)
    pxl_frame = cv.resize(temp_small, (frame.shape[1], frame.shape[0]), interpolation=cv.INTER_NEAREST)

    black_frame = pxl_frame.copy()
    black_frame[:,:] = 0

    signs = "X.-_:,'~;^!=](r+f/)j*c?<>l1Lz7vi|st[nTJuxYIC}Fo{hEPy235Zeba4UVSkw$GXqAdOpm&D9H6QRKg8#0BWN@M"
    l = len(signs)

    for x in range(0, temp_small.shape[0]):
        for y in range(0, temp_small.shape[1]):
            n = temp_small[x,y]
            n = n / 255 * l
            n = int(l - n)
            if n > 1:
                black_frame = cv.putText(black_frame, signs[n], (y*pxl_size, x*pxl_size), cv.FONT_HERSHEY_SIMPLEX, pxl_size / 24, int(temp_small[x,y]/255 * 6) ** 2.5 * 12 , 1)
    cv.imshow("Frame", black_frame)
    out.write((cv.cvtColor(black_frame, cv.COLOR_GRAY2BGR)))
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
out.release()