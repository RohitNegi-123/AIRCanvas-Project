import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

#######################
brushThickness = 10
eraserThickness = 50
########################


folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]
print(header)
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
#
detector = htm.handDetector()
xp, yp = 0, 0
imgCanvas = np.zeros((480, 640, 3), np.uint8)

while True:

    # 1. Import image
    success, img = cap.read()
    print(img.shape)
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        # print(lmList)

        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)

        # 4. If Selection Mode - Two finger are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")
            # # Checking for the click
            if y1<=125:
                if x1>=60 and x1 <=125:
                    header=overlayList[0]
                    drawColor=(190,126,246)
                elif x1>=150 and x1 <=215:
                    header=overlayList[1]
                    drawColor=(50,83,249)
                elif x1>=230 and x1 <=280:
                    header=overlayList[2]
                    drawColor=(0,165,255)
                elif x1>=300 and x1 <=350:
                    header=overlayList[3]
                    drawColor=(0,100,0)
                elif x1>=370 and x1 <=440:
                    header=overlayList[4]
                    drawColor=(190,126,246)
                elif x1>=450 and x1 <=520:
                    header=overlayList[5]
                    drawColor=(239,98,82)
                elif x1>=530 and x1 <=620:
                    header=overlayList[6]
                    drawColor=(0,0,0)
            # if y1 < 125:
            #     if 250 < x1 < 450:
            #         header = overlayList[0]
            #         drawColor = (255, 0, 255)
            #     elif 550 < x1 < 750:
            #         header = overlayList[1]
            #         drawColor = (255, 0, 0)
            #     elif 800 < x1 < 950:
            #         header = overlayList[2]
            #         drawColor = (0, 255, 0)
            #     elif 1050 < x1 < 1200:
            #         header = overlayList[3]
            #         drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        # 5. If Drawing Mode - Index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)

            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

        # # Clear Canvas when all fingers are up
        # if all (x >= 1 for x in fingers):
        #     imgCanvas = np.zeros((480, 640, 3), np.uint8)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    print("Rohit", img.shape,imgInv.shape)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Setting the header image
    img[0:125, 0:640] = header
    # img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Image", img)

    cv2.imshow("Canvas", imgCanvas)
    cv2.imshow("Inv", imgInv)
    cv2.waitKey(1)