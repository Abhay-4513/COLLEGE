int soilmoisture = 0;
const int ledPin = 7;
const int buzzerPin = 8;

void setup()
{
  pinMode(A0, INPUT);
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  soilmoisture = analogRead(A0);
  Serial.println(soilmoisture);
  
  if (soilmoisture <= 200) {
    digitalWrite(buzzerPin, HIGH);
    digitalWrite(ledPin, HIGH);
    delay(200);
    digitalWrite(ledPin, LOW);
    delay(200);
  } else {
    digitalWrite(buzzerPin, LOW);
    digitalWrite(ledPin, LOW);
    delay(10);
  }
}
