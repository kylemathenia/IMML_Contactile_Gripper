#!/usr/bin/env python
"""
This module contains a class for the Oregon State IMML Contactile gripper.
"""

import dynamixel_motors
import time
# If running the script without ROS, rospy logging will not work. Use rospy_shadow instead.
try: import rospy
except: import rospy_shadow as rospy

class Gripper(object):
    """Class for the Oregon State IMML Contactile gripper."""
    def __init__(self):
        # self.motor = dynamixel_motors.XM430_W210(1, 'FT5NSNJ0', 2.0, 57600)
        # self.motor = dynamixel_motors.XM430_W210(1, 'FT5NSNJ0', 2.0, 115200)
        self.motor = dynamixel_motors.XM430_W210(1, 'FT5NSNJ0', 2.0, 4000000)
        self.calibrate()

    def calibrate(self):
        """Finds the motor positions for the maximum open and close gripper positions. Records them with slight safety buffer.
        Sets self.motor.MIN_POS_FULLY_OPEN and self.motor.MAX_POS_FULLY_CLOSED"""
        rospy.loginfo('[CALIBRATE GRIPPER START]')
        self.motor.pos_buffer = 100  # units: 0.0791 degrees
        if self.motor.status != 'initialized': self.motor.initialize()
        # Make sure the motor pos is far away from the zero position to keep limit number positive.
        self.motor.write_torque_mode('off')
        self.motor.write_homing_offset(10000)
        self._calibrate_open()
        self._calibrate_close()
        self.motor.switch_modes('ext_pos_control')
        self.motor.write_goal_pos(self.motor.MIN_POS_FULLY_OPEN)
        rospy.loginfo('[CALIBRATE GRIPPER COMPLETE]')

    def _calibrate_open(self):
        """Finds self.motor.MIN_POS_FULLY_OPEN. Executes the portion of the calibration for opening the gripper."""
        not_done = True
        opening_current = -7
        start_time = time.time()
        if self.motor.torque != 'on': self.motor.write_torque_mode('on')
        if self.motor.mode != 'cur_control': self.motor.switch_modes('cur_control')

        # Start by getting the motor moving. The moving flag controls the program flow.
        while True:
            time_elapsed = time.time() - start_time
            self.motor.write_goal_cur(opening_current)
            moving,error = self.motor.read_moving()
            # If the routine starts with the gripper already fully open the gripper will never start moving.
            # After 2 seconds, assume this is the case. Save MIN_POS_FULLY_OPEN.
            if not moving and time_elapsed > 2:
                while True:  # Make sure that we record a good value. Gripper will break if this is wrong.
                    pos, error = self.motor.read_pos()
                    if not error: break
                self.motor.MIN_POS_FULLY_OPEN = pos + self.motor.pos_buffer
                self.motor.write_goal_cur(0)
                not_done = False
                break
            if moving:
                time.sleep(0.05)  # Give it some time to make sure it is above the moving threshold.
                break

        # Find self.motor.MIN_POS_FULLY_OPEN
        while not_done:
            moving, error = self.motor.read_moving()
            if not moving:  # Gripper is fully open.
                time.sleep(1) # Check that it wasn't just momentarily stuck.
                moving_still, error = self.motor.read_moving()
                if not moving_still:
                    while True:  # Make sure that we record a good value. Gripper will break if this is wrong.
                        pos, error = self.motor.read_pos()
                        if not error: break
                    self.motor.MIN_POS_FULLY_OPEN = pos + self.motor.pos_buffer
                    self.motor.write_goal_cur(0)
                    break
            self.motor.write_goal_cur(opening_current)

        # Move to MIN_POS_FULLY_OPEN (which includes the buffer offset) and stop.
        self.motor.switch_modes('ext_pos_control')
        self.motor.write_goal_pos(self.motor.MIN_POS_FULLY_OPEN)
        time.sleep(0.5)
        rospy.loginfo('[MIN_POS_FULLY_OPEN] {}'.format(self.motor.MIN_POS_FULLY_OPEN))
        time.sleep(0.5)

    def _calibrate_close(self):
        """Finds self.motor.MAX_POS_FULLY_CLOSED. Executes the portion of the calibration for closing the gripper."""
        closing_current = 7
        max_velocity = 20
        if self.motor.torque != 'on': self.motor.write_torque_mode('on')
        if self.motor.mode != 'cur_control': self.motor.switch_modes('cur_control')

        # Get the motor moving in the closed direction.
        while True:
            self.motor.write_goal_cur(closing_current)
            moving,error = self.motor.read_moving()
            if moving:
                time.sleep(0.1)
                break

        # Find self.motor.MAX_POS_FULLY_CLOSED
        while True:
            moving,error = self.motor.read_moving()
            if not moving:
                self.motor.write_goal_cur(closing_current)
                time.sleep(1) # Check that it wasn't just momentarily stuck.
                moving_still,error = self.motor.read_moving()
                if not moving_still:
                    pos, error = self.motor.read_pos()
                    self.motor.MAX_POS_FULLY_CLOSED = pos - self.motor.pos_buffer
                    self.motor.write_goal_cur(0)
                    break
            # Make sure it isn't gaining too much speed.
            vel,error = self.motor.read_vel()
            if vel > max_velocity: self.motor.write_goal_cur(1)
            else: self.motor.write_goal_cur(closing_current)
        rospy.loginfo('[MAX_POS_FULLY_CLOSED] {}'.format(self.motor.MAX_POS_FULLY_CLOSED))

    def __repr__(self):
        pass

def test():
    try:
        g = Gripper()
    except: rospy.loginfo('Test failed.')

def main():
    test()

if __name__ == '__main__':
    main()