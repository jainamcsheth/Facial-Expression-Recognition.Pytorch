# pip install mediapipe

import cv2
import os
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Read the video from specified path
cam = cv2.VideoCapture("./videos/00008.mp4")

try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:
  
  # frame
  currentframe = 0
  skip_frame_to = 1
  while(currentframe < 50):
      
    # reading from frame
    idx,image = cam.read()
  
    if idx:
        # if video is still left continue creating images
        name = './images/annotated_images/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)

        # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Draw face detections of each face.
        if not results.detections:
          continue
        annotated_image = image.copy()
        for detection in results.detections:
          print('Nose tip:')
          print(mp_face_detection.get_key_point(
              detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
          mp_drawing.draw_detection(annotated_image, detection)
        cv2.imwrite(name, annotated_image)
  
        # increasing counters to skip frames
        currentframe += 1
        skip_frame_to += 100
        cam.set(cv2.CAP_PROP_POS_FRAMES, skip_frame_to)
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
