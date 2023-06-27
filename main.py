import cv2
import mediapipe as md
from PIL import Image

md_drawing = md.solutions.drawing_utils
md_drawing_style = md.solutions.drawing_styles
md_pose = md.solutions.pose

count = 0
position = None

cap = cv2.VideoCapture(0)
with md_pose.Pose(
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7) as pose:
    while cap.isOpened():
      success, image = cap.read()
      image = cv2.resize(image, (1080, 720))
      if not success:
        print("empty camera")
        break
      # image = Image.frombytes('RGB', image.size, image.rgb)

      image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
      result=pose.process(image)

      lmlist=[]

      if result.pose_landmarks:
        md_drawing.draw_landmarks(
            image,result.pose_landmarks,md_pose.POSE_CONNECTIONS)
        for id, im in enumerate(result.pose_landmarks.landmark):
          h, w, _= image.shape
          x, y = int(im.x*w), int(im.y*h)
          lmlist.append([id,x,y])
      if len(lmlist) != 0:

          if ((lmlist[12][2] - lmlist[14][2]) >= 15 and (lmlist[11][2] - lmlist[13][2]) >= 15):
              position = "down"
          if ((lmlist[12][2] - lmlist[14][2]) <= 5 and (lmlist[11][2] - lmlist[13][2]) <= 5) and position == "down":
              position = "up"
              count += 1
              print(count)

      cv2.imshow("Push-up counter",cv2.flip(image,1))
      key=cv2.waitKey(1)
      if key ==ord('q'):
        break

cap.release()

