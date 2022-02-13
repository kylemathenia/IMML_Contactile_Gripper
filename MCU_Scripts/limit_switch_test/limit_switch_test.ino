
/*
--limit switches--
Pin 2 to limit switch 1
Pin 4 to limit switch 2
Gnd to limit switch 1 and limit switch 2
*/


const int limSwitch1Pin = 2;
const int limSwitch2Pin = 4;
int switchState1 = 0;
int switchState2 = 0;

String x;

void setup() {
//  // initialize the switch pins as an input with internal pullup resistor
//  pinMode(limSwitch1Pin, INPUT_PULLUP);
//  pinMode(limSwitch2Pin, INPUT_PULLUP);
//  Serial.begin(9600);
Serial.begin(9600);
Serial.setTimeout(500/rate)



}

void loop() {
//  switchState1 = digitalRead(limSwitch1Pin);
//  switchState2 = digitalRead(limSwitch2Pin);
//  
//  if (switchState1 == HIGH) {
//    Serial.println("Switch 1");
//  }
//  else if (switchState2 == HIGH) {
//    Serial.println("Switch 2");
//  }
  if (Serial.available() > 0) {
    char mode = Serial.read();
    long val = Serial.parseInt();
    Serial.readStringUntil('\n');
    Serial.println(mode);
    Serial.println(val);
  }
}







//
//void setup() {
//  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
//}
//
//void loop() {
//  // check if data is available
//  if (Serial.available() > 0) {
//    // read the incoming string:
//    String incomingString = Serial.readStringUntil('\n');
//
//    // prints the received data
//    Serial.print("I received: ");
//    Serial.println(incomingString);
//  }
//}
