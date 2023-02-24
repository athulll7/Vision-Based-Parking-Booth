import cv2
img=cv2.imread("imag1.png")
cv2.imshow("frame",img)
img_size=img.shape
print("SIZE OF COLOR IMAGE=",img_size)

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray_image)

img_size2=gray_image.shape
print("SIZE OF GRAY IMAGE",img_size2)

(thresh,binary)=cv2.threshold(gray_image,100,255,cv2.THRESH_BINARY)
print(thresh)
cv2.imshow("binary",binary)
img_size3=binary.shape
print("SIZE OF B&W IMAGE",img_size3)
cv2.waitKey(1)
