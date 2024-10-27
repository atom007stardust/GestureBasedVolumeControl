import cv2
import mediapipe as mp
import time
import math


class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                              (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)

        return self.lmList, bbox

    def fingersUp(self):
        fingers = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 Fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def findDistance(self, p1, p2, img, draw=True):
        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        return length, img, [x1, y1, x2, y2, cx, cy]


def main():
    pTime = 0
    cap = cv2.VideoCapture(1)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        if len(lmList) != 0:
            if len(lmList) > 4:  # Ensure there are at least 5 landmarks
                print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()

'''
#are minimum code required to run hand tracking
import cv2
import mediapipe as mp
import time #to check the framerate


class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon=0.5, trackCon = 0.5):
        self.mode = mode #we are gonna create an obj, the obj will have its own variable
        #initally assigning it a value provided by the user
        self.maxHands = maxHands
        self.detectionConfidence = detectionCon
        self.trackCon = trackCon

        #related to hand detection model
        #getting values of this diff landmarks is a bit tricky, but we want to be able to tell, the point no 5 of the hand

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands, self.detectionConfidence,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img,draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # this class uses RGB images only, so we need to convert that
        self.results = self.hands.process(imgRGB)  # the process method processes the frame for us and gives us the result
        # #print(results.multi_hand_landmarks) #gives coordinate of hands
        # We can check to see if we have multiple hands or not and extract them, then we can use mpDraw to draw the points

        if (self.results.multi_hand_landmarks):
            # there could be multiple hands, hand no 0, hand no 1 , hand no2 etc, so it goes thru each
            for handLms in self.results.multi_hand_landmarks:  # handLms = hand landmarks
                if draw:
                    # a method in mediapipe helps
                    # mpDraw.draw_landmarks(img, handLms) #we want it to draw the original image, since we are not displaying the rgb image but the original image
                    self.mpDraw.draw_landmarks(img, handLms,
                                          self.mpHands.HAND_CONNECTIONS)  # To draw the hand connections as well
        return img




def findPosition(self, img, handNo = 0, draw=True):
    lmList = []
    #check whether any hands or landmarks were detected or not
    if self.results.multi_hand_landmarks:
        myHand = self.results.multi_hand_landmarks[handNo] #gets all the elements of the hand and then puts them in a list


        # How to track one of these positions for performing a certain task?
        for id, lm in enumerate(handLms.landmark):
            # print(id, lm) #prints the index and x,y,z coordinates of the hand
            # we can use the x and y coordinates
            h, w, c = img.shape
            # we can find the position cx and cy as position of the center
            cx, cy = int(lm.x * w), int(
                lm.y * h)  # originally values were in decimal, we need it in integer
           #print(id, cx, cy)
            lmList.append([id,cx,cy])
            # if id==0:  #It will draw for the ID no 1: base of your palm
            if draw:
                cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
            # if id==4:
            #   cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)
    return lmList

def main():
    pTime = 0
    cTime = 0
    # create video-object
    cap = cv2.VideoCapture(1)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detectfindPosition(img)
        # for setting the frame-rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # displaying the frame rate on the screen
        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 3)

        cv2.imshow("Image", img)  # for displaying

        cv2.waitKey(1)
if __name__ == "__main__":
    main()
#whatever we write in main will be dummy code, used to showcase what this module can do
'''
