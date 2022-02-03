

"""
Stepper calibration routine:
-On startup, user needs to calibrate the linear actuator. Arduino will directly be a linear_actuator_node with ROSSERIAL. 
Control with with control node.  
1) LINEAR ACTUATOR RANGE LIMITS MUST BE SET. INCORRECT SETUP COULD BREAK THE GRIPPER OR LINEAR ACTUATOR.
    
    Lower/upper limits are towards/away from the motor.
    
    a) Full range calibrate (CAUTION: FULL RANGE OF LINEAR ACTUATOR MUST BE CLEAR)
    b) Manually set limits
    
1a) 
    Calibration will begin soon. (Wait 3 seconds)
    
    *** SPACE OR ENTER - EMERGENCY OFF***
    (If stopped, kill the motor and return to previous menu)
    
    Linear actuator calibration complete.
    
1b)
    Set lower limit (limit TOWARDS the motor)
    
    a) Auto - go to lower limit switch (CAUTION: PATH MUST BE CLEAR)
    f/d) Stepper motor - move towards/away from  motor
    e/r) Stepper motor - increase/decrease movement increment 
    e/r) Gripper - open/close
    e/r) Gripper - increase/decrease movement increment 
    s) Set lower limit
    i) Show info again
    SPACE OR ENTER) EMERGENCY OFF
    
    **** Once lower limt set...
    
    Set upper limit (limit AWAY from the  motor)
    
    a) Auto - go to upper limit switch (CAUTION: PATH MUST BE CLEAR)
    f/d) Stepper motor - move towards/away from  motor
    e/r) Stepper motor - increase/decrease movement increment 
    e/r) Gripper - open/close
    e/r) Gripper - increase/decrease movement increment 
    s) Set lower limit
    i) Show info again
    SPACE OR ENTER) EMERGENCY OFF
    
    Linear actuator calibration complete.
    
Once complete, go to UI home page.

TODO: ui_node:
    -In home screen, add an option to set linear actuator limits.
    -Change the direct contol menu to also include the stepper motor.
    -Service routines to set the motor limit values in the linear_actuator_node to make sure it happens.
TODO: linear_actuator_node:
    -Service routines to set the motor limit values in the linear_actuator_node to make sure it happens.
    -Hard code the acceleration and max speed profiles. Potentially, make max speed adjustable. Figure out what they
    should be.
    -Figure out if this will need different modes. Perhpas direct speed control mode where speed commands are constantly
    published while the motor constantly publishes the current position, or position mode where the stepper is supposed
    to just go to a position (as in direct control).
    -Figure out how to keep the motor position constant even though the motor will be shutting off and on. Does it reset?
TODO: control_node:
    -Need to publish stepper speed or or position commands, similar to Dynamixel.
    -Need to subscribe to stepper motor position values.

"""

class Test(object):
    def __init__(self):
        pass
    def func(self):

    self.func.p = "hello"

