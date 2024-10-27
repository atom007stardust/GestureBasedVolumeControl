import math
import cv2
import mediapipe as mp
import pyautogui

#create a line b/w 4 and 8
x1 = y1 =x2 = y2 =0 #all 4 variables are equal to 0
webcam = cv2.VideoCapture(1)
my_hands = mp.solutions.hands.Hands() #initializes the hand-tracking model to detect and track hands
drawing_utils = mp.solutions.drawing_utils #a module within medidapipe to draw annotations on images or video-frames


while True:
    _, image = webcam.read() #returns two variables
    image = cv2.flip(image, 1) #flipping through y-axis
    frame_height, frame_width,_  = image.shape
    #we need to provide a wait function
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #mediapipe expects images in rgb format, whereas opencv captures it in bgr format, hence the conversion is required
    output = my_hands.process(rgb_image) #to detect and track the hands using mediapipe tracking model
    hands = output.multi_hand_landmarks #collect all the hand landmarks
    #a list where each element represents the landmarks of one hand detected
    if hands: #if hands are available
        for hand in hands:
            drawing_utils.draw_landmarks(image,hand) #draw connections on the hand
            landmarks = hand.landmark #collect all the hand landmarks in landmarks
            for id, landmark in enumerate(landmarks):
                x = int (landmark.x * frame_width) #x-coordiante of the landmark converted from normalized to pixel
                y = int (landmark.y * frame_height) #y-coordinate of the landmark
                if (id==8): #index finger
                    cv2.circle(img = image, center = (x,y), radius = 8, color = (255,0,255), thickness = 3)
                    x1 = x
                    y1 = y
                if (id ==4): #thumb finger
                    cv2.circle(img = image, center = (x,y), radius = 8, color = (255,255,0), thickness = 3)
                    x2 = x
                    y2 = y


        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)

        if dist > 100: #means that they are at a high distance then we need to increase volume
            pyautogui.press("volumeup")
        elif (dist<50):
            pyautogui.press("volumedown")


    cv2.imshow("Hand Volume control using python",image) #this fn shows the video


    key = cv2.waitKey(10) #waits for 10 milli seconds
    if key == 27: #if we pressed the escape key
        break #close the window
webcam.release()
cv2.destroyAllWindows()


