#!/usr/bin/env python
"""
This module contains the node for the test stand stepper motor.
"""

import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'support'))
import roslib; roslib.load_manifest('contactile_gripper')
import rospy
from contactile_gripper.srv import *
from std_msgs.msg import String,Float32,Int64,Int32
from contactile_gripper.msg import Float32List,Int32List
import stepper
import time


class StepperNode(object):
    """ROS node for the Dynamixel motor. Max com speed is ~62hz for read or write operation. This is both reading
    and writing, so rate is 30hz. """
    def __init__(self):
        self.stepper = stepper.Stepper()
        rospy.init_node('stepper_node', anonymous=False, log_level=rospy.INFO)

        # Publishers
        self.stepper_pos_pub = rospy.Publisher('Stepper_Pos',Int64, queue_size=1)
        self.cur_pos = None
        self.limit_switch_pub = rospy.Publisher('Limit_Switch_Status', Int32List, queue_size=1)
        self.upper_switch_status = None
        self.lower_switch_status = None

        # Subscribers
        self.stepper_cmd_sub = rospy.Subscriber('Stepper_Cmd', String, self.stepper_cmd_callback, queue_size=1)

        # Services
        self.stepper_off_srv = rospy.Service('stepper_off_srv', StepperOff, self.srv_handle_stepper_off)
        self.stepper_set_limit_srv = rospy.Service('stepper_set_limit_srv', StepperSetLimit, self.srv_handle_stepper_set_limit)

        self.pub_loop_rate = 60 # Hz
        self.pub_loop_rate_obj = rospy.Rate(self.pub_loop_rate)
        self.upper_lim = None
        self.lower_lim = None
        self.cmd_mode = 'off'
        self.cmd_val = None

        rospy.on_shutdown(self.shutdown_function)
        self.pub_loop()


    ######################## Subscriber and service callbacks ########################
    def srv_handle_stepper_off(self, req):
        self.stepper.write('<x_0>')
        self.cmd_mode = 'off'
        return StepperOffResponse('Stepper off')

    def srv_handle_stepper_set_limit(self, req):
        limit_value = 0
        if req.action == 'clear':
            self.lower_lim = None
            self.upper_lim = None
        elif req.switch == 'upper' and req.action == 'set':
            self.upper_lim = self.cur_pos
            limit_value = self.upper_lim
        elif req.switch == 'lower' and req.action == 'set':
            self.lower_lim = self.cur_pos
            limit_value = self.lower_lim
        else:
            rospy.logwarn('StepperSetLimit service failed. Key error with action: {} or switch: {}'.format(req.action, req.switch))
        return StepperSetLimitResponse(limit_value)

    def stepper_cmd_callback(self, msg):
        cmd = msg.data.split('_')
        self.cmd_mode = cmd[0]
        self.cmd_val = int(cmd[1])


    ######################## Main loop ########################
    def pub_loop(self):
        self.stepper.clean_before_read_start()
        while not rospy.is_shutdown():
            self.read_data_update_vals()
            self.publish_data()
            self.write_command()
            self.pub_loop_rate_obj.sleep()

    ######################## Other ########################

    def read_data_update_vals(self):
        lower_switch_status, upper_switch_status, cur_pos, com_success = self.stepper.read()
        rospy.loginfo('{} {} {} {}'.format(lower_switch_status, upper_switch_status, cur_pos, com_success))
        if com_success:
            self.cur_pos = int(cur_pos)
            self.upper_switch_status = int(upper_switch_status)
            self.lower_switch_status = int(lower_switch_status)

    def publish_data(self):
        self.stepper_pos_pub.publish(self.cur_pos)
        self.limit_switch_pub.publish([self.upper_switch_status,self.lower_switch_status])

    def write_command(self):
        if self.cmd_mode == 'position':
            self.check_limits_write_pos()
        elif self.cmd_mode == 'speed':
            self.check_limits_write_speed()
        elif self.cmd_mode == 'off':
            pass

    def check_limits_write_pos(self):
        goal_pos = self.cmd_val
        cmd = '<p_' + str(goal_pos) + '>'
        if self.upper_lim is None and self.lower_lim is None:
            self.stepper.write(cmd)
        elif self.upper_lim is not None and self.lower_lim is None:
            if goal_pos < self.upper_lim: self.stepper.write(cmd)
        elif self.upper_lim is None and self.lower_lim is not None:
            if goal_pos > self.lower_lim: self.stepper.write(cmd)
        elif goal_pos < self.upper_lim and goal_pos > self.lower_lim:
            self.stepper.write(cmd)

    def check_limits_write_speed(self):
        new_speed = self.cmd_val
        cmd = '<s_' + str(new_speed) + '>'
        if self.upper_lim is None and self.lower_lim is None:
            self.stepper.write(cmd)
        elif self.upper_lim is not None and self.lower_lim is None:
            if self.cur_pos < self.upper_lim or new_speed < 0: self.stepper.write(cmd)
        elif self.upper_lim is None and self.lower_lim is not None:
            if self.cur_pos > self.lower_lim or new_speed > 0: self.stepper.write(cmd)
        # Both an upper and lower limit and cur pos is within limits
        elif self.cur_pos < self.upper_lim and self.cur_pos > self.lower_lim:
            self.stepper.write(cmd)
        # Both an upper and lower limit and cur pos is beyond upper limit
        elif self.cur_pos > self.upper_lim:
            if new_speed < 0: self.stepper.write(cmd)
        # Both an upper and lower limit and cur pos is beyond lower limit
        elif self.cur_pos < self.lower_lim:
            if new_speed > 0: self.stepper.write(cmd)


    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        self.stepper.serial.close()

def main():
    _ = StepperNode()

if __name__ == '__main__':
    main()
