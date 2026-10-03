// C++ code
//
void setup()
{
  pinMode(13, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop()
{
  digitalWrite(13, HIGH);
  digitalWrite(11, LOW);
  digitalWrite(7, LOW);
  delay(2000);
  
  digitalWrite(13, LOW);
  digitalWrite(11, HIGH);
  digitalWrite(7, LOW);
  delay(2000);
  
  digitalWrite(13, LOW);
  digitalWrite(11, LOW);
  digitalWrite(7, HIGH);
  delay(2000);
}
