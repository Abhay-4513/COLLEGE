#include <Servo.h>

Servo myservo;  
int potpin = 0; 
int val;
int angle;  

void setup() {
  myservo.attach(9); 
  Serial.begin(9600);
}

void loop() {
  val = analogRead(potpin);
  angle = map(val, 0, 1023, 0, 180);
  myservo.write(angle);
  
  Serial.print("Potentiometer Value : ");
  Serial.print(val);
  Serial.print("\ ");
  Serial.print("Rotation : ");
  Serial.println(angle);
  Serial.println();
  delay(15);
}
