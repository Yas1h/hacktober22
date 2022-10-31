import cv2

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
capture.set(10,150)
nPlateCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
color = (255,0,255)
while True:
    isTrue, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in numberPlates:
        area = w*h
        if area>500:
            cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
            cv2.putText(img, "Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            imgRoi = img[y:y+h, x:x+w]
        # cv.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break