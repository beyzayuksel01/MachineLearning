import cv2
import mediapipe as mp
webcam=cv2.VideoCapture(0)
mp_cizim=mp.solutions.drawing_utils
mp_butunsel=mp.solutions.holistic
with mp_butunsel.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as butun:
    while True:
        kontrol,camera=webcam.read()
        resim_rgb=cv2.cvtColor(camera,cv2.COLOR_BGR2RGB)
        #tespit
        sonuc=butun.process(resim_rgb)
        resim=cv2.cvtColor(resim_rgb,cv2.COLOR_RGB2BGR)
        mp_cizim.draw_landmarks(camera,sonuc.face_landmarks,mp_butunsel.FACEMESH_CONTOURS,mp_cizim.DrawingSpec((0,255,0),0,0))
        if cv2.waitKey(20)==27:
            break
        cv2.imshow("Yuz Tanima",camera)