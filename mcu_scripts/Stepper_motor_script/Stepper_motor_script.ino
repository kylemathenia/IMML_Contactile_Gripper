#include <AccelStepper.h>
#include <arduino-timer.h>

/* Incoming communication protocol:
 * Format: <[mode]_[value]>
 * p = position mode
 * s = speed mode
 * x = off/passive mode
 * Example: "<p_500>" -> position mode, goal position of 500
 * Example: "<x_1>" -> off mode, 1 is unused, but 
 */

/* Outgoing communication protocol:
 * Format: <[lim switch 1 status]_[lim switch 2 status]_[current position]>
 * lim switch status: 1 if engaged, 0 if not.
 * Example: "<1_0_543>" -> lim switch 1 engaged, lim switch 2 not engaged, current position is 543.
 */

/*
Wiring info: 
--stepper--
Pin 9 to Dir+
Pin 8 to Pul+
Pin 7 to Ena+
Gnd to Pul-, Dir-, and Ena-
***Make sure the power supply voltage matches the spec for the motor.
--limit switches--
Pin 2 to limit switch 1 normally closed terminal
Pin 4 to limit switch 2 normally closed terminal
Gnd to limit switch 1 and limit switch 2 common terminal
*/


// pins
const int limSwitch1Pin = 2;
const int limSwitch2Pin = 4;
const int dirPin = 9;
const int pulPin = 8;
const int enaPin = 7;

// lim switch
int switch1State;
int switch2State;

// stepper
//char cmd_mode = 'x';
long goal_vel;
long cmd_pos = 0;
long cur_pos = 0;
int motorStatus; //0 for off, 1 for on.
// Interface mode, direction Digital 9 (CW), pulses Digital 8 (CCW),enable mode on.
AccelStepper stepper(AccelStepper::DRIVER, 8, 9, true);

// other
int rate = 40; //Hz. Rate to send outgoing data. 
auto timer = timer_create_default(); // Create a timer to be used with function to send data out. 
long timeOfLastCommand = 0;
long stepperOffTimeout = 60000;  // milliseconds
int motorTimeoutFlag = 0;
String delimeter = "_";
String start_char = "<";
String end_char = ">";
long baudrate = 2500000;
//long baudrate = 9600;

const byte buffSize = 40;
char inputBuffer[buffSize];
const char startMarker = '<';
const char endMarker = '>';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newDataFromPC = false;

char cmd_mode[buffSize] = {0};




void setup()
{
  limSwitchSetup();
  stepperSetup();
  Serial.begin(baudrate);
  // Give the timer functions to run and the period to run them. 
  timer.every(1000/rate, sendData); //Only sends data at the rate specified to not overwhelm the serial com with outgoing messages.
  timer.every(120000, checkMotorTimeout);
}

void loop()
{
  updateSwitchStatus();
  cur_pos = stepper.currentPosition();
  checkSerial();
  executeCommand();
  timer.tick(); // Run the functions to send data if it is time. 
}





/* ########################## Functions ##########################*/

void limSwitchSetup()
{
  // initialize the switch pins as an input with internal pullup resistor
  pinMode(limSwitch1Pin, INPUT_PULLUP);
  pinMode(limSwitch2Pin, INPUT_PULLUP);
}

void stepperSetup()
{
  //Need to set enable pin after construction per constructor documentation. 
  stepper.setEnablePin(7);
  //Invert the enable pin so that enable/disable functions aren't backwards. 
  stepper.setPinsInverted(false,false,true);
  //setting up some values for maximum speed and maximum acceleration
  stepper.setMaxSpeed(200000); //SPEED = Steps / second
  stepper.setAcceleration(40000); //ACCELERATION = Steps /(second)^2
  stepper.setCurrentPosition(0); 
  motorOff(); //disable outputs so the motor is not getting warm (no current)
}


bool checkMotorTimeout(void *) {
  if (((millis() - timeOfLastCommand) > stepperOffTimeout) && motorStatus == 1){
    motorTimeoutFlag = 1;
  }
  return true; //Return true to repeat the function.
}

bool sendData(void *)
{
  Serial.println(start_char + switch1State + delimeter + switch2State + delimeter + cur_pos + end_char);
  Serial.flush();
  return true; //Return true to repeat the function.
}


void resetMotorTimeout() {
  timeOfLastCommand = millis();
  motorTimeoutFlag =0;
}

void updateSwitchStatus()
{
  switch1State = digitalRead(limSwitch1Pin);
  switch2State = digitalRead(limSwitch2Pin);
}


void checkSerial() {
  if(Serial.available() > 0) {
    char x = Serial.read();
    if (x == endMarker) {
      readInProgress = false;
      newDataFromPC = true;
      inputBuffer[bytesRecvd] = 0;
      parseData();
    }
    
    if(readInProgress) {
      inputBuffer[bytesRecvd] = x;
      bytesRecvd ++;
      if (bytesRecvd == buffSize) {
        bytesRecvd = buffSize - 1;
      }
    }
    if (x == startMarker) { 
      bytesRecvd = 0; 
      readInProgress = true;
    }
  }
}

void parseData() {
  //Splits the new message into parts and sets vars. 
  char * strtokIndx; // this is used by strtok() as an index
  strtokIndx = strtok(inputBuffer,"_");      // get the first part - the string
  strcpy(cmd_mode, strtokIndx);
  
  strtokIndx = strtok(NULL, "_"); // this continues where the previous call left off

  if (strcmp(cmd_mode, "p") == 0){
    cmd_pos = atol(strtokIndx); 
    stepper.moveTo(cmd_pos);
  }
  else if (strcmp(cmd_mode, "s") == 0){
    goal_vel = atol(strtokIndx); 
    stepper.setSpeed(goal_vel);
  }
  resetMotorTimeout();
}


void executeCommand()
{
  //Turn on the motor if it isn't but should be. 
  if (strcmp(cmd_mode, "x") != 0 && motorTimeoutFlag == 0 && motorStatus == 0){
    motorOn();
  }

  if (switch1State == 1 || switch2State == 1){
    switchOnExecute();
  }
  else{
    normalExecute();
  }
}


void switchOnExecute(){
  // If the limit switches are engaged and the goal is the wrong direction, stop.
  if (switch1State == 1 && strcmp(cmd_mode, "p") == 0 && cmd_pos < cur_pos){
    limitStop();
  }
  else if (switch1State == 1 && strcmp(cmd_mode, "s") == 0 && goal_vel < 0){
    limitStop();
  }
  else if (switch2State == 1 && strcmp(cmd_mode, "p") == 0 && cmd_pos > cur_pos){
    limitStop();
  }
  else if (switch2State == 1 && strcmp(cmd_mode, "s") == 0 && goal_vel > 0){
    limitStop();
  }
  else{
    normalExecute();
  }
}

void normalExecute(){
  if (strcmp(cmd_mode, "x") == 0 || (motorTimeoutFlag == 1 && motorStatus == 1)){
    motorOff();
  }
  else if (strcmp(cmd_mode, "p") == 0){
    stepper.run(); //Move one step.
  }
  else if (strcmp(cmd_mode, "s") == 0){
    stepper.runSpeed(); //Move one step.
  }
}


void limitStop(){
  stepper.stop();
//  motorOff();
  goal_vel=0;
  cmd_pos=cur_pos;
  stepper.moveTo(cmd_pos);
  stepper.setSpeed(goal_vel);
}

void motorOff()
{
  stepper.disableOutputs();
  motorStatus = 0;
}

void motorOn()
{
  stepper.enableOutputs();
  motorStatus = 1;
}
