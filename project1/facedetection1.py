import cv2
from time import sleep
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
anterior = 0
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass
    ret, camera = video_capture.read()
    gray = cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(camera, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Video', camera)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Video', camera)
video_capture.release()
cv2.destroyAllWindows()
