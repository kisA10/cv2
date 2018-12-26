import numpy as np
import cv2

cap0 = cv2.VideoCapture(1)

cap0.set(6,cv2.VideoWriter_fourcc(*'MJPG'))
cap0.set(5,10)
cap0.set(4,1920)
cap0.set(3,1080)

# cap1 = cv2.VideoCapture(1)
# cap2 = cv2.VideoCapture(3)
# cap3 = cv2.VideoCapture(4)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'H264')
fps = 30
size = (1920,1080)

out = cv2.VideoWriter('output.avi',fourcc, fps, size)

while(cap0.isOpened()):
    ret0, frame0 = cap0.read()
    # ret1, frame1 = cap1.read()
    # ret2, frame2 = cap2.read()
    # ret3, frame3 = cap3.read()

    
    if ret0==True:
        #frame = cv2.flip(frame1,0)

        # write the flipped frame
        out.write(frame0)

        cv2.imshow('frame0',frame0)
        # cv2.imshow('frame1',frame1)
        # cv2.imshow('frame2',frame2)
        # cv2.imshow('frame3',frame3)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap0.release()
# cap1.release()
# cap2.release()
# cap3.release()
out.release()
cv2.destroyAllWindows()
