int trig = 9; 
int echo = 10;
int led1 = 11; 
int led2 = 12;
int led3 = 13;

long duration = 0; 
int cm = 0; 
int in = 0;

void setup()
{
  pinMode(trig, OUTPUT); 
  pinMode(echo, INPUT);
  pinMode(led1, OUTPUT); 
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT); 
  Serial.begin(9600); 
  Serial.println("Serial Started..."); 
}

void loop()
{
  digitalWrite(trig, LOW); 
  digitalWrite(trig, HIGH); 
  digitalWrite(trig, LOW);
  
  int duration = pulseIn (echo, HIGH); 
  cm = duration*0.034/2;
  in = duration*0.0133/2;
  
  Serial.println(in); 
  
  if (in >= 108) {
    digitalWrite(led3, LOW); 
    digitalWrite(led2, LOW); 
    digitalWrite(led1, LOW); 
    delay(1000); 
    digitalWrite(led3, HIGH); 
    digitalWrite(led2, LOW); 
    digitalWrite(led1, LOW); 
    delay(1000); 
  }
  
   else if (in < 108 && in > 36){
    digitalWrite(led3, LOW); 
    digitalWrite(led2, LOW);
    digitalWrite(led1, LOW);
    delay(600); 
    digitalWrite(led3, LOW); 
    digitalWrite(led2, HIGH); 
    digitalWrite(led1, LOW); 
    delay(600); 
  }
  
   else if (in <= 36 ){
    digitalWrite(led3, LOW); 
    digitalWrite(led2, LOW); 
    digitalWrite(led1, LOW); 
    delay(300);
    digitalWrite(led3, LOW); 
    digitalWrite(led2, LOW); 
    digitalWrite(led1, HIGH); 
    delay(300); 
  }
}