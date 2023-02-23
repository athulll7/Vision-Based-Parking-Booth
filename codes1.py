import cv2

img = cv2.imread('0.png')
cv2.imshow("Color Image", img) #frame
imgsize=img.shape
print("Color Image",imgsize)

gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray Image", gray_image)
imgsize1=gray_image.shape
print("Gray Image",imgsize1)

if(len(imgsize1)==3):
    print("Color Image")
elif(len(imgsize1)==2):
    print("Gray Image")
    
thresh, binary)=cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY) 
print(thresh)

cv2.imshow("Binary",binary)
cv2.imwrite("BW Image.png",binary)
cv2.waitKey(1)
