int timer = 100;           // The higher the number, the slower the timing.

void setup() {
  // use a for loop to initialize each pin as an output:
  for (int thisPin = 2; thisPin < 13; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}

void loop() {
 // Exam1();
//  Exam2();
  ledrun1();
 // ledrun2();
}

void ledrun1()
{
  const int pins[13] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 3};

  for (int i = 0; i < 10; ++i) {
    digitalWrite(pins[i], HIGH);
    digitalWrite(pins[i + 1], HIGH);
    digitalWrite(pins[i + 2], HIGH);
    
    delay(timer);
    
    digitalWrite(pins[i], LOW);
    digitalWrite(pins[i + 1], LOW);
    digitalWrite(pins[i + 2], LOW);
  }
}

void ledrun2()
{
  for (int thisPin = 2; thisPin < 13; thisPin++) {
    if(thisPin < 5){
      digitalWrite(thisPin+8,LOW);
      digitalWrite(thisPin, HIGH);
      delay(timer);
    }
    else{
      digitalWrite(thisPin-3,LOW);
      digitalWrite(thisPin, HIGH);
      delay(timer);      
    }

  }
}

void Exam1()
{
    // loop from the lowest pin to the highest:
  for (int thisPin = 2; thisPin < 13; thisPin++) {
    // turn the pin on:
    digitalWrite(thisPin, HIGH);
    delay(timer);
    // turn the pin off:
    digitalWrite(thisPin, LOW);
  }

  // loop from the highest pin to the lowest:
  for (int thisPin = 12; thisPin >= 2; thisPin--) {
    // turn the pin on:
    digitalWrite(thisPin, HIGH);
    delay(timer);
    // turn the pin off:
    digitalWrite(thisPin, LOW);
  }
}

void Exam2()
{
    // loop from the lowest pin to the highest:
  for (int thisPin = 2; thisPin < 13; thisPin++) {
    // turn the pin on:
    digitalWrite(thisPin, HIGH);
    delay(timer);
    // turn the pin off:
   // digitalWrite(thisPin, LOW);
  }

  // loop from the highest pin to the lowest:
  for (int thisPin = 12; thisPin >= 2; thisPin--) {
    // turn the pin on:
    digitalWrite(thisPin,LOW);
    delay(timer);
    // turn the pin off:
   // digitalWrite(thisPin, LOW);
  }
}