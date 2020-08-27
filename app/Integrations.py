import cv2, os
import numpy as np
from playsound import playsound
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)


# tracker = cv2.TrackerMOSSE_create()  # Opencv-contrib-python
tracker =  cv2.TrackerCSRT_create()  # Works Well
# tracker = cv2.TrackerBoosting_create()
# tracker = cv2.TrackerKCF_create()

success, img = cap.read()  # To take frame
# Create bounding box # bbox statands for bounding box that we are going to create in the Tracking window.
bbox = cv2.selectROI('Tracking', img, False)
tracker.init(img, bbox)  # Initialising Tracker


def qr():
    with open('Authentication.txt') as f:
        auth_list = f.read().splitlines()
        for i in decode(img):
            v_sound = 0
            myData = i.data.decode('utf-8')
            if myData in auth_list:
                x = 'Authorised'
                mycolor = (0, 255, 0)
                v_sound = 1
            else:
                x = 'Un-authorised'
                mycolor = (0, 0, 255)
                v_sound = 2
            pts = np.array([i.polygon], np.int32)
            pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            pts2 = i.rect
            cv2.putText(img, x, (pts2[0], pts2[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, mycolor, 2)


def drawBox():
    # bbox is not a list that's why we did this.
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x+w), (y+h)), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 75),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    qr()

def get_frame():
    while True:
        timer = cv2.getTickCount()  # frames per second
        success, img = cap.read()
        success, bbox = tracker.update(img)  # Updating bounding box
        # We have different ypy of trackers provided by open CV
        if success:
            drawBox()
        else:
            cv2.putText(img, "Lost", (75, 75),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
        cv2.putText(img, str(int(fps)), (75, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow('Tracking', img)
        ret, jpeg = cv2.imencode('.jpeg', img)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

        return jpeg.tobytes() 
