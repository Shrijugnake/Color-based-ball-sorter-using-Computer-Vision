#include <Servo.h>
Servo myservo1;   
  
String inByte;
int pos;
   

void setup() {
 
  myservo1.attach(9);
  
  Serial.begin(9600);
}

void loop()
{    
  if(Serial.available())  // if data available in serial port
    { 
    inByte = Serial.readStringUntil('\n'); // read data until newline
    pos = inByte.toInt();   // change datatype from string to integer 
        
        myservo1.write(pos);     // move servo
        delay(1000);
       // Serial.print("Servo1 in position: ");  
      //  Serial.println(inByte);
       }
}
