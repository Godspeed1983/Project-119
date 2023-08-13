import cv2

video = cv2.VideoCapture("C:/Users/Adit Kadiyan/Downloads/c119-ObjectTracking-1-4-main/c119-ObjectTracking-1-4-main/bb3.mp4")

#Load tracker
tracker=cv2.TrackerCSRT_create()

#Read the frame
ret,img=video.read()

#Select the bounding box on the image
bbox=cv2.selectROI("Tracking",img,False)

tracker.init(img,bbox)

print(bbox)

def drawBox(img,bbox):
    x,y,w,h=int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,h+y),(255,0,255),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

while True:
    check , img = video.read()

    success,bbox=tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    cv2.imshow("result",img)

    if waitKey(25) == 32:
        print("Stopped")
        break
video.release()
cv2.destroyAllWindows()
