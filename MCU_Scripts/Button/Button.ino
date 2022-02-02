/*
  When button is pressed, do something. 
*/

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;         // the number of the pushbutton pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the pushbutton pin as an input with internal pullup resistor.:
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is LOW:
  if (buttonState == LOW) {
    Serial.println(buttonState);
  }
  delay(10); //Debounce.
}
