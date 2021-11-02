import cv2
import numpy as np

lowerBound = np.array([170, 100, 80])
upperBound = np.array([180, 256, 256])

# cam= cv2.VideoCapture(0)
while True:
    img = cv2.imread('roman.jpg')
    img =cv2.resize(img,(612,612))
    # convert BGR to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('original image',img)
    # create the Mask

    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    dilated = cv2.dilate(mask, None, iterations=6)
    contour, _= cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for countours in contour:
        x, y, w, h = cv2.boundingRect(countours)
        if cv2.contourArea(countours) < 10:
            continue
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    # cv2.imshow("mask", mask)

    cv2.imshow("image", img)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
        break
