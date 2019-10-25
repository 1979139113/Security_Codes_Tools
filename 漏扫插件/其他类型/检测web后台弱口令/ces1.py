import cv2
filename='input.jpg'

face_cascade=cv2.CascadeClassifier('D:/opencv/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,5)
for (x,y,h,w) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.namedWindow('faces Detected!')
cv2.imshow('faces Detected!',img)
cv2.imwrite('faces.jpg',img)
cv2.waitKey(0)
---------------------
作者：自闭少女Monana
来源：CSDN
原文：https://blog.csdn.net/serena9636/article/details/52530446
版权声明：本文为博主原创文章，转载请附上博文链接！