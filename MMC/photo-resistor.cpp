int sensorValue = 0;
int ledPin = 5;
int ldrPin = A0;

void setup(){
	Serial.begin(9600);
  	pinMode(ledPin,OUTPUT);
    pinMode(ldrPin,INPUT);
}

void loop(){
  	sensorValue = analogRead(ldrPin);
  	sensorValue = map(sensorValue, 26,923,255,0);
  	Serial.println(sensorValue);
  	analogWrite(ledPin,sensorValue);
}