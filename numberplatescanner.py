import cv2

cam = cv2.VideoCapture(0)

count = 0
while True:

    a, img = cam.read()
    
    key = cv2.waitKey(1)
    cv2.putText(img,"PLACE THE NUMBER PLATE INSIDE THE BOX",(180,160),cv2.FONT_HERSHEY_TRIPLEX,0.4,(255,255,255),1)
    cv2.rectangle(img,(80,200),(560,350),(255,255,255),2)
    cv2.imshow("image",img)
    print(key)
    if(key == ord('q')):
        count=count+1
        img_name=str(count)+".png"
        print("captured")

        cv2.imwrite(img_name,img)
        break

cam.release()
cv2.destroyAllWindows()
