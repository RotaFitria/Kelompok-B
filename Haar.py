import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

img = cv2.imread('img_path')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

print (len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
   
cv2.imwrite('test.jpg', img)
cv2.waitKey()
