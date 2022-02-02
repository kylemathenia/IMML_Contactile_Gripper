#include <AccelStepper.h>

/* Example script for a 4 pin bipolar stepper motor with motor driver using AccelStepper library and Arduino.
 *  
 *  Documentation at: https://www.airspayce.com/mikem/arduino/AccelStepper/classAccelStepper.html
 */

/* Command format: [letter][number of steps to move] [max speed]
 * Example command: "c500 100" -> close 500 steps with a max speed of 100
 * 
 * o = open (CW) // needs steps and speed values
 * c = close (CCW) //needs steps and speed values
 * s = stop right now! // just the 's' is needed
 */

/*
Wiring info: 
***Arduino - Driver***
Pin 9 to Dir+
Pin 8 to Pul+
Pin 7 to Ena+
Gnd to Pul-, Dir-, and Ena-
***Driver - Stepper***
Wire according to stepper motor wiring diagram. 
If no diagram, do a continuity check to find matching coil pairs A+/A- B+/B- https://www.youtube.com/watch?v=S0pGKgos498
***Power Supply - Driver***
Make sure the power supply is providing the correct voltage..
*/

// pins
const int dirPin = 9;
const int pulPin = 8;
const int enaPin = 7;

// variables
long commandedSteps = 0;
long stepCounter = 0;      
long commandedMaxSpeed = 0;           //delay between two steps, received from the computer
long receivedAcceleration = 0;    //acceleration value from computer
char receivedLetter;             //First char of commanded string
bool runAllowed = false;
 
// Initialize AccelStepper object with interface mode 1, direction pin (9), pulses pin (8)
AccelStepper stepper(1, 8, 9);
 
void setup()
{
  Serial.begin(9600); //define baud rate
  Serial.println("Testing Accelstepper"); //print a message

  // Set the enable pin after init per constructor documentation to be able to use disable/enableOutputs methods. 
  stepper.setEnablePin(7);
  //setting up some default values for maximum speed and maximum acceleration
  stepper.setMaxSpeed(2000); //SPEED = Steps / second
  stepper.setAcceleration(1000); //ACCELERATION = Steps /(second)^2
  stepper.disableOutputs(); //disable outputs, so the motor is not getting hot (no current)
}

 
void loop()
{
  checkCommands(); //If there is a new command on the serial port, handle them. 
  executeCommands(); //Execute command.
}
 
 
void executeCommands()
{
  if (stepCounter < abs(commandedSteps) && runAllowed == true)
  {
    stepper.enableOutputs();
    Serial.print("Running...\n");
    stepper.run(); //step the motor (this will step the motor by 1 step at each loop)
    stepCounter ++;
  }
  else if (runAllowed == true)  //Command just completed
  {
    runAllowed = false;
    stepper.disableOutputs(); // disable power
    Serial.print("Current Position: ");
    Serial.println(stepper.currentPosition());
  }
}


void checkCommands() //If there are new commands, change things. 
{  
// *** If new command, stepper.enableOutputs(); //enable pins ***

  if (Serial.available() > 0) //If there is a new command.
  {
    receivedLetter = Serial.read(); //First byte assumed to be command letter. 
    commandedSteps = Serial.parseFloat(); //Next float that can be parsed is value for the steps
    commandedMaxSpeed = Serial.parseFloat(); //Next float that can be parsed is value for the speed
    stepCounter = 0;
    Serial.println(receivedLetter);
    Serial.println(commandedSteps);
    Serial.println(commandedMaxSpeed);
    

    if (receivedLetter == 'o'){
      stepper.enableOutputs();
      runAllowed = true;
      stepper.setMaxSpeed(commandedMaxSpeed);
      stepper.move(commandedSteps);
    }
    else if (receivedLetter == 'c'){
      stepper.enableOutputs();
      runAllowed = true;
      stepper.setMaxSpeed(commandedMaxSpeed);
      stepper.move(-1*commandedSteps);
    }
    else if(receivedLetter == 's'){
      stepper.stop(); //stop motor
      stepper.disableOutputs(); //disable power
    }
    else{
      Serial.println("Invalid command");
    }
  }
}
