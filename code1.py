import cv2 

cam = cv2.VideoCapture(0) #object creation,by class

count=0
a, img = cam.read() #image array,a status  T/F
cv2.imshow("Camera", img)
key = cv2.waitKey(1) #frame holding time
print(key)
