# GestureBasedVolumeControl
 This Python app uses MediaPipe and OpenCV to track hand gestures and adjust system volume via PyAutoGUI. It measures the thumb-index finger distance to increase or decrease volume, offering a hands-free way to control sound levels.

## Overview

This project allows users to control the system volume using hand gestures. The application leverages the MediaPipe library for hand tracking and OpenCV for image processing. By measuring the distance between the thumb and index finger, the program adjusts the system volume accordingly.

## Features

- Hand gesture tracking with MediaPipe.
- Volume adjustment based on finger distance.
- Real-time control of system volume using PyAutoGUI.

## Requirements
- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/atom007stardust/FingerVolumeControl.git
    ```

2. Navigate to the project directory:
    ```bash
    cd FingerVolumeControl
    ```

3. Install the required packages:
    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

## Usage

1. Connect a webcam to your computer.
2. Run the script:
    ```bash
    python volume_control.py
    ```

3. Adjust the distance between your thumb and index finger to increase or decrease the system volume.

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

