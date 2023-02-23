import cv2 

cam = cv2.VideoCapture(0) #object creation,by class

count=0
while True: 

    a, img = cam.read() #image array,a status  T/F
    
    cv2.imshow("Camera", img)
    key = cv2.waitKey(1) #frame holding time
    print(key)
    if(key == ord('q')): #to return asci value
        imgname=str(count)+".png"
        cv2.imwrite(imgname,img)
        count=count+1
        
        print("Captured")
        break

cam.release() 
cv2.destroyAllWindows()