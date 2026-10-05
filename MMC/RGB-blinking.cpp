// C++ code
//
int redPin = 13;
int bluePin = 12;
int greenPin = 8;

void setup()
{
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

void loop()
{
	setColor(255, 0, 0); //red
  	delay(1000);
  
  	setColor(0, 255, 0); //green
  	delay(1000);
  
  	setColor(0, 0, 255); //blue
  	delay(1000);
  
  	setColor(255, 255, 0); //yellow
  	delay(1000);
  
  	setColor(255, 0, 255); //purple
  	delay(1000);
  
  	setColor(0, 255, 255); //aqua
  	delay(1000);
}

void setColor(int red, int green, int blue)
{
  #ifdef COMMON_ANODE
  	red = 255-red;
  	green = 255-green;
  	blue = 255-blue;
  #endif
  	analogWrite(redPin,red);
    analogWrite(bluePin,blue);
    analogWrite(greenPin,green);
  
}
