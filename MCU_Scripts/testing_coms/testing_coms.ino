//This script echos back an incoming string. 

//The idea here is to write a string and decode the message into useful parts. This can be done by indexing the positions of the string. 

String msg;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}

//Perhaps message is x32_y59_z20_\n

void loop() {
  if (Serial.available()>0){
 msg = Serial.readStringUntil('\n');
 String x=msg.substring(1,3); //Arduino code is 0 indexed. Substring is index exclusive. 
 Serial.println(x);
}
}
