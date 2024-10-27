# GestureBasedVolumeControl
 This Python app uses MediaPipe and OpenCV to track hand gestures and adjust system volume via PyAutoGUI. It measures the thumb-index finger distance to increase or decrease volume, offering a hands-free way to control sound levels.

## Code Overview
Mediapipe Hand Tracking: Mediapipe's Hands model detects hands and landmarks in real-time.
Landmark Detection: Key landmarks (thumb and index finger tips) are tracked and used for volume control.
Volume Control: Uses pyautogui to send volumeup and volumedown commands based on the distance between landmarks.

## Hand Landmarks
The Mediapipe hand tracking model detects 21 hand landmarks, each representing a unique point on the hand. Here are some key landmarks used in this code:

4: Thumb tip
8: Index finger tip
This project draws a line between these two landmarks to measure the distance between the thumb and index finger, adjusting the volume based on this distance.

## Features

- Hand gesture tracking with MediaPipe.
- Volume adjustment based on finger distance.
- Real-time control of system volume using PyAutoGUI.

## Requirements
- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation of packages

 Install the required packages:
    ```
    pip install opencv-python mediapipe pyautogui
    ```

## Code Explanation

- **MediaPipe**: Used for detecting and tracking hand landmarks.
- **OpenCV**: Used for image processing and drawing.
- **PyAutoGUI**: Used for simulating volume up and down key presses.
- 
## Controls
Move the index finger tip (Landmark 8) and thumb tip (Landmark 4) close together to decrease the volume.
Increase the distance between these two points to increase the volume.

