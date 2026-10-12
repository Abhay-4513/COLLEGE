C++
const int led = 7;
const int buzzer = 12;

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int gasValue = analogRead(A0);
  Serial.print("Gas Value=");
  Serial.println(gasValue);

  if (gasValue > 300)
  {
    digitalWrite(led, HIGH);
    digitalWrite(buzzer, HIGH);
    tone(buzzer, 1000);
    Serial.println("Gas Detected");
  }
  else
  {
    digitalWrite(led, LOW);
    digitalWrite(buzzer, LOW);
    noTone(buzzer);
    Serial.println("Normal Air");
  }
  delay(1000);
}