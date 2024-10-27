#bare minimum code required to run hand tracking
import cv2
import mediapipe as mp
import time #to check the framerate

#create video-object
cap = cv2.VideoCapture(1)

#related to hand detection model
#getting values of this diff landmarks is a bit tricky, but we want to be able to tell, the point no 5 of the hand
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #this class uses RGB images only, so we need to convert that
    results = hands.process(imgRGB) #the process method processes the frame for us and gives us the result
    #print(results.multi_hand_landmarks) #gives coordinate of hands
    #We can check to see if we have multiple hands or not and extract them, then we can use mpDraw to draw the points

    if(results.multi_hand_landmarks):
        #there could be multiple hands, hand no 0, hand no 1 , hand no2 etc, so it goes thru each
        for handLms in results.multi_hand_landmarks:  #handLms = hand landmarks
            # How to track one of these positions for performing a certain task?
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm) #prints the index and x,y,z coordinates of the hand
                #we can use the x and y coordinates
                h, w ,c = img.shape
                #we can find the position cx and cy as position of the center
                cx, cy = int(lm.x * w ), int(lm.y *h) #originally values were in decimal, we need it in integer
                print(id,cx,cy)
               # if id==0:  #It will draw for the ID no 1: base of your palm
                cv2.circle(img, (cx,cy),10,(255,0,255),cv2.FILLED)
               # if id==4:
                 #   cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)

                #a method in mediapipe helps
               # mpDraw.draw_landmarks(img, handLms) #we want it to draw the original image, since we are not displaying the rgb image but the original image
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #To draw the hand connections as well

    #for setting the frame-rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #displaying the frame rate on the screen
    cv2.putText(img, str(int(fps)), (10,50),cv2.FONT_HERSHEY_COMPLEX,1, (255,0,255), 3)




    cv2.imshow("Image",img) #for displaying

    cv2.waitKey(1)
