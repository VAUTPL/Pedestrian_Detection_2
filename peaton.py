################################################
#     Universidad Tecnica Particular de Loja   #  
################################################
#     Professor:                               #
#     Rodrigo Barba    lrbarba@utpl.edu.ec     #
################################################
#   Students:                                  #
#   Víctor Pérez      vfperez@utpl.edu.ec      # 
#   Cristian Vera     crvera3@utpl.edu.ec      #
################################################


import numpy as np
import cv2
 
#Load the template and initialize the webcam
#HOG Algorithm
hog = cv2.HOGDescriptor()
hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
cap = cv2.VideoCapture(0)
# variables 
c_punt=[244,0,0]
n_peatons=0
while(True):
    x1=0;
    y1=0;
    
    #We read a frame and keep it.
    ret,img1 = cap.read()
    #turn the image
    img = cv2.flip(img1,1)
    #We convert the image to black and white
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    #We look for the coordinates if there is one and we keep their position
    
    found,x=hog.detectMultiScale(gray, winStride=(8,8), padding=(32,32), scale=1.09)
     
    #A rectangle is drawn in the coordinates of each person
    for (x,y,w,h) in found:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
    #A circle is drawn in the center of each person
        cv2.circle(img,(x+35,y+80), 10, (0,255,0), 0)
    #Calculate to find the center of the rectangle
        x1=x+(w/2)
        y1=y+(h/2)
       
   #Draw a line in the center to do the counting of people
    cv2.line(img,(300,0),(300,500),(c_punt),5)
    print x1
   # Opening range for counting
    if(x1>=295 and x1<=305):
   # Count the people
        n_peatons=n_peatons+1
   #Number of pedestrians
    cv2.putText(img,str(n_peatons), (220,40), cv2.FONT_HERSHEY_TRIPLEX, 1,(0,0,255),2)
    cv2.putText(img,str('PEATON'), (50,40), cv2.FONT_HERSHEY_TRIPLEX, 1,(0,0,255),2)
   #Name of the window
    cv2.imshow('CAMARA',img)
   #With the 'x' key we exit the program
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
   
cap.release()
cv2.destroyAllWindows()


