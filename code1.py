import cv2 

cam = cv2.VideoCapture(0) #object creation,by class

count=0
a, img = cam.read() #image array,a status  T/F
