#This program will detect two colors B and R
#and will print that it got detected
#area is speciied for each color balls/objects.



import cv2
import numpy as np
import time
import imutils
import serial


#cap=cv2.VideoCapture(0)

print("Star of program")
usbport = 'COM6'

arduino = serial.Serial(usbport, 9600, timeout=1)

a=1
b=1
cap=cv2.VideoCapture(1)
while True:
   
    
    ret,frame=cap.read()
    blurred_frame=cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
    #hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    
    
    cv2.imshow("Its video",frame)
   
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126,255,255])
    #lower_blue = np.array([94, 80, 2])
    #upper_blue = np.array([255,255,126])

    #lower_green = np.array([40,40,40])  #[40,40,40]
    #upper_green = np.array([70,255,255]) #[70,255,255]

    low_red=np.array([0,120,70])
    high_red=np.array([10,255,255])
    #low_red=np.array([0,50,50])
    #high_red=np.array([10,255,255])
    
    
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    #mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3=cv2.inRange(hsv,low_red, high_red)
    
    cnts1= cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1=imutils.grab_contours(cnts1)
     
    #cnts2= cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cnts2=imutils.grab_contours(cnts2)

    cnts3= cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3=imutils.grab_contours(cnts3)
    
    

    for cont in cnts1:   #Blue color
        area1=cv2.contourArea(cont)
        
        #print(area)

        if 1500<area1<4500: #EDIT THIS AREA WHEN DISTANCE BETWEEN CAMERA AND OBJECT CHANGES

            #while True:                                             # create loop
            if(a==1):
                command1 = str(int(62))
                arduino.write(command1.encode())                  #Servo 1 closed gripp          # write position to serial port
                #reachedPos = str(arduino.readline())            # read serial port for arduino echo
                #print(reachedPos)                              # print arduino echo to console
         
                #time.sleep(0.2)       
                print("Blue Sorted")
                #print(reachedPos)
                a=2
                b=1
                break
                print("Error")


    
    
    for cont in cnts3:           #Red color
        area3=cv2.contourArea(cont)

       # print(area)

        if 1500<area3<4500:
          if(b==1):
            #while True:                                             # create loop

                       
            
            command1 = str(int(117))
            arduino.write(command1.encode())                  #Servo 1 closed gripp          # write position to serial port
            #reachedPos = str(arduino.readline())            # read serial port for arduino echo
            #print(reachedPos)                              # print arduino echo to console
         
            #time.sleep(5)
            #time.sleep(0.2)
            print("Red Sorted")
            #print(reachedPos)
            a=1
            b=2
            break
            print("Error")

    cv2.imshow("Its video",frame)
    #cv2.imshow("Its video",frame)
    key=cv2.waitKey(1)
    if key==27:                     #Esc==27
        break

cap.release()
cv2.destroyAllWindows()

arduino.close()
