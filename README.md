# Push-up Detector

The Push-up Detector is an AI model that analyzes the actions of an athlete using a device camera. It detects whether the athlete is performing push-ups or any other skill, such as pull-ups, in front of the camera. The detector uses the MediaPipe library for pose estimation and landmark tracking.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)
- PIL (`pip install pillow`)

## Usage

1. Clone the repository or download the code files.

2. Install the required dependencies mentioned in the "Requirements" section.

3. Connect a webcam or ensure that the device camera is accessible.

4. Run the `pushup_detector.py` script:


5. The script will open a window showing the webcam feed and draw the detected pose landmarks on the frame.

6. Perform push-ups in front of the camera. If the athlete performs a push-up, the script will display "PUSHUP" on the screen. If any other skill is performed, it will display "NOT A PUSH UP".

7. Press the 'q' key to exit the program.

## Customization

- You can adjust the minimum detection and tracking confidence thresholds in the `md_pose.Pose` initialization to change the sensitivity of the pose detection.

- To modify the push-up detection logic, you can update the landmark positions and the conditions for determining a push-up action in the code.

## Notes

- The push-up detector relies on the accurate detection and tracking of pose landmarks. Lighting conditions, camera angle, and the athlete's clothing may affect the accuracy of the detection. Adjustments and fine-tuning may be required for optimal performance.

- The current implementation assumes a basic push-up motion, but it may not accurately detect variations or improper form. The model is intended as a demonstration and may not be suitable for rigorous analysis or training purposes.

- For any issues or suggestions, please feel free to open an issue or submit a pull request in the repository.

