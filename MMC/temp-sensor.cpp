int temp = A1;
int Rpin = 2;
int Bpin = 3;
int Gpin = 4;

void setup() {
  pinMode(temp, INPUT);
  pinMode(Rpin, OUTPUT);
  pinMode(Bpin, OUTPUT);
  pinMode(Gpin, OUTPUT);

  Serial.begin(9600);
}

void turnoff() {
  digitalWrite(Gpin, LOW);
  digitalWrite(Bpin, LOW);
  digitalWrite(Rpin, LOW);
}

void loop() {
  int sensor = analogRead(temp);

  int temp1 = map(sensor, 20, 358, -40, 125);

  Serial.println(temp1);

  if (temp1 <= 10) {
    turnoff();
    digitalWrite(Gpin, HIGH);
  }
  else if (temp1 <= 30) {
    turnoff();
    digitalWrite(Bpin, HIGH);
  }
  else {
    turnoff();
    digitalWrite(Rpin, HIGH);
  }

}
