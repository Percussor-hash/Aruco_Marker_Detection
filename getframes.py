import cv2 
import cv2.aruco as aruco
import numpy as np



# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture("mega3.mp4")
i = 0
 
while(cap.isOpened()):
    ret, frame = cap.read()
     
    # This condition prevents from infinite looping
    # incase video ends.
    if ret == False:
        break
     
    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    i += 1
 
cap.release()
cv2.destroyAllWindows()

def findAruco(img, marker_size=6,total_markers=250,draw=True):
  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')
  arucoDict=aruco.Dictionary_get(key)
  arucoParam=aruco.DetectorParameters_create()
  bbox,ids,_=aruco.detectMarkers(gray,arucoDict,parameters=arucoParam)
  print(ids)
  if draw:
    aruco.drawDetectedMarkers(img,bbox)
  return bbox,ids


j = 1  
sonic =  'Frame'+str(j)+'.jpg'
while i!=j:
    sonic =  'Frame'+str(j)+'.jpg'
    img = cv2.imread(sonic)
    img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)    
    bbox,ids = findAruco(img) 
    j = j + 1 
    if cv2.waitKey(1)==113:
        break
    cv2.imshow("img",img)
cv2.destroyAllWindows()