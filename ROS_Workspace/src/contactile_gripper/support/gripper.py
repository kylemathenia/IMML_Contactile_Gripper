#!/usr/bin/env python
"""
This module contains a class for the Oregon State IMML Contactile gripper.
"""

import dynamixel_motors
import time
import atexit

# If running the script without ROS, rospy logging will not work. Use rospy_shadow instead.
try: import rospy
except: import rospy_shadow as rospy

class Gripper(object):
    """Class for the Oregon State IMML Contactile gripper."""
    def __init__(self,fast_start=False):
        self.motor = dynamixel_motors.XM430_W210(1, 'FT5NSNJ0', 2.0, 4000000)
        self.grip_range = 3000  # Found from experimentation. Used for fast start method.
        self.mode_options = set(self.motor.operating_modes.keys())
        self.mode_options.add('off')
        self.mode = None
        self.pos_buffer = 100  # units: 0.0791 degrees. Gives buffer from the actual physical hard stops to prevent damage.
        atexit.register(self.shutdown_function)

        self.pos_p_gain = 200
        self.pos_i_gain = 100
        self.pos_d_gain = 400
        self.init_motor_settings()
        if fast_start: self.fast_start()
        else: self.calibrate()
        com_error = self.switch_modes('off')

    def init_motor_settings(self):
        com_error = self.switch_modes('off')
        self.motor.write_pos_p_gain(self.pos_p_gain)
        self.motor.write_pos_i_gain(self.pos_i_gain)
        self.motor.write_pos_d_gain(self.pos_d_gain)
        self.motor.write_current_limit(200)
        # Make sure the motor pos is far away from the zero position to keep limit number positive.
        self.motor.write_homing_offset(100000)

    def calibrate(self):
        """Finds the motor positions for the maximum open and close gripper positions. Records them with slight safety buffer.
        Sets self.motor.MIN_POS_FULLY_OPEN and self.motor.MAX_POS_FULLY_CLOSED"""
        rospy.loginfo('[CALIBRATE GRIPPER START]')
        self._calibrate_open()
        self.fully_open()
        self._calibrate_close()
        self.fully_open()
        time.sleep(1.5)  # Wait to fully open.
        self.grip_range = self.motor.MAX_POS_FULLY_CLOSED - self.motor.MIN_POS_FULLY_OPEN
        rospy.loginfo('Gripper range: {}'.format(self.grip_range))
        rospy.loginfo('[CALIBRATE GRIPPER COMPLETE]')

    def _calibrate_open(self):
        """Finds the fully open gripper position, self.motor.MIN_POS_FULLY_OPEN."""
        opening_current = -7
        if self.mode != 'cur_control':
            com_error = self.switch_modes('cur_control')

        # Get the motor moving in the open direction.
        self.motor.write_goal_cur(opening_current)
        time.sleep(0.5)
        # Find self.motor.MIN_POS_FULLY_OPEN
        while True:
            moving, error = self.motor.read_moving()
            if not moving:  # Gripper is fully open.
                time.sleep(1) # Check that it wasn't just momentarily stuck.
                moving_still, error = self.motor.read_moving()
                if not moving_still:
                    while True:  # Make sure that we record a good value. Gripper will break if this is wrong.
                        pos, error = self.motor.read_pos()
                        if not error: break
                    self.motor.MIN_POS_FULLY_OPEN = pos + self.pos_buffer
                    self.motor.write_goal_cur(0)
                    break

    def _calibrate_close(self):
        """Finds self.motor.MAX_POS_FULLY_CLOSED. Executes the portion of the calibration for closing the gripper."""
        closing_current = 10
        max_velocity = 25
        if self.mode != 'cur_control':
            com_error = self.switch_modes('cur_control')

        # Get the motor moving in the closed direction.
        self.motor.write_goal_cur(closing_current)
        time.sleep(0.25)

        # Find self.motor.MAX_POS_FULLY_CLOSED
        while True:
            moving,error = self.motor.read_moving()
            if not moving:
                self.motor.write_goal_cur(closing_current)
                time.sleep(1) # Check that it wasn't just momentarily stuck.
                moving_still,error = self.motor.read_moving()
                if not moving_still:
                    pos, error = self.motor.read_pos()
                    # Allow the gripper to close a little more than it stopped at.
                    self.motor.MAX_POS_FULLY_CLOSED = pos + self.pos_buffer
                    self.motor.write_goal_cur(0)
                    break
            # Make sure it isn't gaining too much speed.
            vel,error = self.motor.read_vel()
            if vel > max_velocity: self.motor.write_goal_cur(closing_current//3)
            else: self.motor.write_goal_cur(closing_current)
        rospy.loginfo('[MAX_POS_FULLY_CLOSED] {}'.format(self.motor.MAX_POS_FULLY_CLOSED))

    def fast_start(self):
        """Instead of doing the full calibration routine at startup, just assume the closed gripper position based on
        the hard coded gripper range."""
        self._calibrate_open()
        self.motor.MAX_POS_FULLY_CLOSED = self.motor.MIN_POS_FULLY_OPEN + self.grip_range
        self.fully_open()
        time.sleep(1.5) # Wait to fully open.

    def fully_open(self):
        """Move to MIN_POS_FULLY_OPEN (which includes the buffer offset)."""
        com_error = self.switch_modes('cur_based_pos_control')
        self.motor.write_goal_pos(self.motor.MIN_POS_FULLY_OPEN)
        rospy.loginfo('[MIN_POS_FULLY_OPEN] {}'.format(self.motor.MIN_POS_FULLY_OPEN))

    def switch_modes(self,mode):
        """Combines the dynamixel torque mode and operating mode into a single gripper mode. If not 'off', the motor
        torque is on."""
        rospy.logdebug('[switch_modes] {}'.format(mode))
        assert mode in self.mode_options
        com_error = True
        while com_error:
            if mode == 'off':
                com_error = self.motor.write_torque_mode('off')
                self.motor.write_led(0)
            elif mode in self.mode_options:
                com_error = self.motor.switch_modes(mode)
                self.motor.write_led(1)
        self.mode = mode
        return com_error

    def shutdown_function(self):
        self.switch_modes('off')

def test():
    g = Gripper()
    rospy.loginfo('Test passed.')

def main():
    test()

if __name__ == '__main__':
    main()