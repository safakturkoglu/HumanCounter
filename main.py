import time
import math
import cv2
import os
import numpy as np
from vidgear.gears import CamGear
from firebase import firebase
import time
import datetime
import pytz

confid = 0.5
thresh = 0.5

# Firebase Connection
firebase = firebase.FirebaseApplication("https://humancounter-eefad-default-rtdb.firebaseio.com/", None)

# Timezone settings
tz = pytz.timezone('Europe/Istanbul')


# Youtube Stream Connection
stream = CamGear(
    source="https://www.youtube.com/watch?v=AdUw5RdyZxI", 
    stream_mode=True,
    logging=True
).start()

# Calibration needed for each video
angle_factor = 0.3
H_zoom_factor = 1.5

# Read class labels
labelsPath = "./coco.names"
LABELS = open(labelsPath).read().strip().split("\n")

np.random.seed(42)


# Yolov3 weights and config path
weightsPath = "./yolov3.weights"
configPath = "./yolov3.cfg"

###### use this for faster processing (caution: slighly lower accuracy) ###########

#weightsPath = "./yolov3-tiny.weights"  ## https://pjreddie.com/media/files/yolov3-tiny.weights
#configPath = "./yolov3-tiny.cfg"       ## https://github.com/pjreddie/darknet/blob/master/cfg/yolov3-tiny.cfg

# Model configurations
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

writer = None
(W, H) = (None, None)

# For each video frame 
while True:

    time_now = datetime.datetime.now(tz).strftime("%d-%m-%Y %H:%M:%S")

    (grabbed, frame) = True, stream.read()

    if not grabbed:
        break

    (H, W) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()

    boxes = []
    confidences = []
    classIDs = []

    for output in layerOutputs:

        for detection in output:

            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if LABELS[classID] == "person":
                if confidence > confid:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confid, thresh)

    if len(idxs) > 0:

        status = []
        idf = idxs.flatten()
        close_pair = []
        s_close_pair = []
        center = []
        co_info = []

        for i in idf:
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            cen = [int(x + w / 2), int(y + h / 2)]
            center.append(cen)
            cv2.circle(frame, tuple(cen),1,(0,0,0),1)
            co_info.append([w, h, cen])

            status.append(0)

        crowded_number = 0

        for i in idf:
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            if w < 90 and h < 90:
              crowded_number += 1
              cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    tot_str = "TOTAL COUNT: " + str(crowded_number)
    print(tot_str)

    cv2.putText(frame, tot_str, (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Save image path
    path = "/content/gdrive/MyDrive/task-1/images/" + str(time_now) + ".jpg"
    # Save image
    cv2.imwrite(os.path.join(path),frame)

    # Data for Firebase
    data = {
        'Time': time_now,
        'Count': crowded_number
    }

    # Firebase post data
    result = firebase.post('/Counter',data)
    # Sleep 30 seconds
    time.sleep(30)
