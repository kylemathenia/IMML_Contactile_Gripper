#!/usr/bin/env python
"""
This module contains the node for the test stand stepper motor.
"""

import roslib; roslib.load_manifest('contactile_gripper')
from contactile_gripper.srv import StepperOff
from contactile_gripper.srv import StepperSetLimit
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Int64
from std_msgs.msg import Int32
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
        self.upper_lim_switch_pub = rospy.Publisher('Upper_Lim_Switch_Status', Int32, queue_size=1)
        self.upper_switch_status = None
        self.lower_lim_switch_pub = rospy.Publisher('Lower_Lim_Switch_Status', Int32, queue_size=1)
        self.lower_switch_status = None

        # Subscribers
        self.stepper_cmd_sub = rospy.Subscriber('Stepper_Cmd', String, self.stepper_cmd_callback, queue_size=1, buff_size = 100)

        # Services
        self.stepper_off_srv = rospy.Service('stepper_off_srv', StepperOff, self.srv_handle_stepper_off)
        self.stepper_set_limit_srv = rospy.Service('stepper_set_limit_srv', StepperSetLimit, self.srv_handle_stepper_set_limit)

        self.pub_loop_rate = 40 # Hz
        self.pub_loop_rate_obj = rospy.Rate(self.pub_loop_rate)
        self.upper_lim = None
        self.lower_lim = None

        rospy.on_shutdown(self.shutdown_function)
        self.pub_loop()

    def pub_loop(self):
        self.stepper.clean_before_read_start()
        while not rospy.is_shutdown():
            com_success = self.update_vals()
            if com_success: self.publish_data()
            self.pub_loop_rate_obj.sleep()

    def update_vals(self):
        lower_switch_status, upper_switch_status, cur_pos, com_success = self.stepper.read()
        rospy.loginfo('{} {} {} {}'.format(lower_switch_status, upper_switch_status, cur_pos, com_success))
        if com_success:
            self.cur_pos = int(cur_pos)
            self.upper_switch_status = int(upper_switch_status)
            self.lower_switch_status = int(lower_switch_status)
        return com_success

    def publish_data(self):
        self.stepper_pos_pub.publish(self.cur_pos)
        self.upper_lim_switch_pub.publish(self.upper_switch_status)
        self.lower_lim_switch_pub.publish(self.lower_switch_status)

    def srv_handle_stepper_off(self, req):
        self.stepper.write('<x_0>')
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
        else: rospy.logwarn('StepperSetLimit service failed. Key error with action: {} or switch: {}'.format(req.action,req.switch))
        return StepperSetLimitResponse(limit_value)

    def stepper_cmd_callback(self,msg):
        val = int(msg.data)
        new_pos = self.cur_pos + val
        cmd = '<p_' + msg.data + '>'
        if self.upper_lim is None and self.lower_lim is None:
            self.stepper.write(cmd)
        elif self.upper_lim is not None and self.lower_lim is None:
            if new_pos < self.upper_lim: self.stepper.write(cmd)
        elif self.upper_lim is None and self.lower_lim is not None:
            if new_pos > self.lower_lim: self.stepper.write(cmd)
        elif new_pos < self.upper_lim and new_pos > self.lower_lim:
            self.stepper.write(cmd)

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        self.stepper.serial.close()

def main():
    _ = StepperNode()

if __name__ == '__main__':
    main()
