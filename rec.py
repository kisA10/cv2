import numpy as np
import cv2
import datetime

width = 1920
height = 1080
# width = 640
# height = 480

fourcc = cv2.VideoWriter_fourcc(*'h264')

cap0 = cv2.VideoCapture(0)

cap0.set(cv2.CAP_PROP_FOURCC,fourcc)
cap0.set(cv2.CAP_PROP_FPS,30)
cap0.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

# cap1 = cv2.VideoCapture(1)
# cap2 = cv2.VideoCapture(3)
# cap3 = cv2.VideoCapture(4)

# Define the codec and create VideoWriter object

fps = 30
size = (width,height)



out = cv2.VideoWriter('/media/kis/data/output.mkv',fourcc, fps, size)
# out = cv2.VideoWriter('output.avi',fourcc, fps, size)

while(cap0.isOpened()):
    ret0, frame0 = cap0.read()
    # ret1, frame1 = cap1.read()
    # ret2, frame2 = cap2.read()
    # ret3, frame3 = cap3.read()

    
    if ret0==True:
        #frame = cv2.flip(frame1,0)

        # write the flipped frame

        time = datetime.datetime.now().strftime('%Y %m %d %H:%M:%S')
        depth = 'depth : 1645'
        # print(time)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame0, time, (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame0, depth, (50, 650), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('frame0',frame0)
        cv2.moveWindow('frame0',0,0)
        # cv2.imshow('frame1',frame1)
        # cv2.imshow('frame2',frame2)
        # cv2.imshow('frame3',frame3)
        # out.write(frame0)
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
