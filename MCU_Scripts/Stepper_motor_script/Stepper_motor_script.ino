#include <AccelStepper.h>

/* Example script for AccelStepper with Arduino

/* o = open (CW) // needs steps and speed values
 * c = close (CCW) //needs steps and speed values
 * a = set acceleration // needs acceleration value
 * n = stop right now! // just the 'n' is needed
 * Command format: [letter][number of steps to move] [max speed]
 * Example command: "c500 100" -> close 500 steps with a max speed of 100
 */

/*
Wiring info: 
--stepper--
Pin 9 to Dir+
Pin 8 to Pul+
Pin 7 to Ena+
Gnd to Pul-, Dir-, and Ena-
--limit switches--
Pin 2 to limit switch 1
Pin 4 to limit switch 2
Gnd to limit switch 1 and limit switch 2
*/


//const int limSwitch1Pin = 2;         // the number of the pushbutton pin
//
//// variables will change:
//int buttonState = 0;         // variable for reading the pushbutton status
//
//void setup() {
//  // initialize the pushbutton pin as an input with internal pullup resistor.:
//  pinMode(limSwitch1Pin, INPUT_PULLUP);
//  Serial.begin(9600);
//}
//
//void loop() {
//  // read the state of the pushbutton value:
//  buttonState = digitalRead(limSwitch1Pin);
//
//  // check if the pushbutton is pressed. If it is, the buttonState is LOW:
//  if (buttonState == LOW) {
//    Serial.println(buttonState);
//  }
//  delay(10); //Debounce.
//}







 // pins
const int limSwitch1Pin = 2;
pinMode(limSwitch1Pin, INPUT_PULLUP)
const int limSwitch2Pin = 4;
pinMode(limSwitch1Pin, INPUT_PULLUP)
const int dirPin = 9;
const int pulPin = 8;
const int enaPin = 7;
pinMode(limSwitch1Pin, INPUT_PULLUP)


// variables
//int buttonState = 0;         // variable for reading the pushbutton status
long receivedMMdistance = 0; //distance in mm from the computer
long receivedDelay = 0; //delay between two steps, received from the computer
long receivedAcceleration = 0; //acceleration value from computer
char receivedCommand; //character for commands
/* s = Start (CCW) // needs steps and speed values
 * o = open (CCW) // needs steps and speed values
 * c = close (CW) //needs steps and speed values
 * a = set acceleration // needs acceleration value
 * n = stop right now! // just the 'n' is needed
 */
 
bool newData, runallowed = false; // booleans for new data from serial, and runallowed flag
 
 
 
// Interface mode 1, direction Digital 9 (CW), pulses Digital 8 (CCW)
AccelStepper stepper(1, 8, 9);
// TODO: Need to verify if this is right. Need to set enable pin after construction per constructor documentation. 
stepper.setEnablePin(7)
 
 
void setup()
{
  Serial.begin(9600); //define baud rate
  Serial.println("Testing Accelstepper"); //print a message
 
  //setting up some default values for maximum speed and maximum acceleration
  stepper.setMaxSpeed(2000); //SPEED = Steps / second
  stepper.setAcceleration(1000); //ACCELERATION = Steps /(second)^2
 
  stepper.disableOutputs(); //disable outputs, so the motor is not getting warm (no current)
 
 
}
 
void loop()
{

//   // read the state of the pushbutton value:
//  switchState = digitalRead(switchPin);
// 
//   // check if the pushbutton is pressed.
//   // if it is, the buttonState is HIGH:
//   if (switchState == HIGH) {
//     // turn Motor off:
//     Serial.println("Double coil steps");
//   myMotor->step(0, FORWARD, DOUBLE); 
//   myMotor->step(0, BACKWARD, DOUBLE);
//   } else {
//     // turn Motor: on.
//      Serial.println("Double coil steps");
//   myMotor->step(2000, FORWARD, DOUBLE); 
//   myMotor->step(2000, BACKWARD, DOUBLE);
//   }
 
  checkSerial(); //check serial port for new commands
 
  continuousRun2(); //method to handle the motor
 
}
 
 
void continuousRun2() //method for the motor
{
  if (runallowed == true)
  {
    if (abs(stepper.currentPosition()) < receivedMMdistance) //abs() is needed because of the '<'
    {
      stepper.enableOutputs(); //enable pins
      stepper.run(); //step the motor (this will step the motor by 1 step at each loop)
    }
    else //program enters this part if the required distance is completed
    {
     
      runallowed = false; //disable running -> the program will not try to enter this if-else anymore
      stepper.disableOutputs(); // disable power
      Serial.print("POS: ");
      Serial.println(stepper.currentPosition()); // print pos -> this will show you the latest relative number of steps
      stepper.setCurrentPosition(0); //reset the position to zero
      Serial.print("POS: ");
      Serial.println(stepper.currentPosition()); // print pos -> this will show you the latest relative number of steps; we check here if it is zero for real
    }
 
 
  }
  else //program enters this part if the runallowed is FALSE, we do not do anything
  {
    return;
 
  }
}


void disableOutputs() 
{
  
}

void enableOutputs() 
{
  
}


void checkSerial() //method for receiving the commands
{  
  //switch-case would also work, and maybe more elegant
 
  if (Serial.available() > 0) //if something comes
  {
    receivedCommand = Serial.read(); // this will read the command character
    newData = true; //this creates a flag
  }
 
  if (newData == true) //if we received something (see above)
  {
    //START - MEASURE
    if (receivedCommand == 's') //this is the measure part
    {
      //example s 2000 500 - 2000 steps (5 revolution with 400 step/rev microstepping) and 500 steps/s speed
      runallowed = true; //allow running
     
 
      receivedMMdistance = Serial.parseFloat(); //value for the steps
      receivedDelay = Serial.parseFloat(); //value for the speed
 
      Serial.print(receivedMMdistance); //print the values for checking
      Serial.print(receivedDelay);
      Serial.println("Measure "); //print the action
      stepper.setMaxSpeed(receivedDelay); //set speed
      stepper.move(receivedMMdistance); //set distance
 
    }
    //START - OPEN
    if (receivedCommand == 'o') //OPENING
    {
      //example o 2000 500 - 2000 steps (5 revolution with 400 step/rev microstepping) and 500 steps/s speed
      runallowed = true; //allow running
     
 
 
      receivedMMdistance = Serial.parseFloat(); //value for the steps
      receivedDelay = Serial.parseFloat(); //value for the speed
 
      Serial.print(receivedMMdistance); //print the values for checking
      Serial.print(receivedDelay);
      Serial.println("OPEN "); //print the action
      stepper.setMaxSpeed(receivedDelay); //set speed
      stepper.move(receivedMMdistance); //set distance
 
    }
 
    //START - CLOSE
    if (receivedCommand == 'c') //CLOSING - Rotates the motor in the opposite direction as opening
    {
      //example c 2000 500 - 2000 steps (5 revolution with 400 step/rev microstepping) and 500 steps/s speed; will rotate in the other direction
      runallowed = true; //allow running
     
 
 
      receivedMMdistance = Serial.parseFloat(); //value for the steps
      receivedDelay = Serial.parseFloat(); //value for the speed
 
      Serial.print(receivedMMdistance);  //print the values for checking
      Serial.print(receivedDelay);
      Serial.println("CLOSE "); //print action
      stepper.setMaxSpeed(receivedDelay); //set speed
      stepper.move(-1 * receivedMMdistance); ////set distance - negative value flips the direction
 
    }
 
    //STOP - STOP
    if (receivedCommand == 'n') //immediately stops the motor
    {
      runallowed = false; //disable running
       
      stepper.setCurrentPosition(0); // reset position
      Serial.println("STOP "); //print action
      stepper.stop(); //stop motor
      stepper.disableOutputs(); //disable power
 
    }
 
    //SET ACCELERATION
    if (receivedCommand == 'a') //Setting up a new acceleration value
    {
      runallowed = false; //we still keep running disabled, since we just update a variable
     
      receivedAcceleration = Serial.parseFloat(); //receive the acceleration from serial
 
      stepper.setAcceleration(receivedAcceleration); //update the value of the variable
 
      Serial.println("ACC Updated "); //confirm update by message
 
    }
 
  }
  //after we went through the above tasks, newData becomes false again, so we are ready to receive new commands again.
  newData = false;
  
}
