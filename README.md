# GestureBasedVolumeControl
 This Python app uses MediaPipe and OpenCV to track hand gestures and adjust system volume via PyAutoGUI. It measures the thumb-index finger distance to increase or decrease volume, offering a hands-free way to control sound levels.

## Overview

This project allows users to control the system volume using hand gestures. The application leverages the MediaPipe library for hand tracking and OpenCV for image processing. By measuring the distance between the thumb and index finger, the program adjusts the system volume accordingly.

##Hand Landmarks
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

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or fixes.

## Acknowledgements

- MediaPipe for hand tracking capabilities.
- OpenCV for image processing.
- PyAutoGUI for simulating keyboard inputs.

