#!/usr/bin/env python
"""
This module contains the node for the test stand stepper motor.
"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Int64
import stepper
import time

class TestStandNode(object):
    """ROS node for the Dynamixel motor. Max com speed is ~62hz for read or write operation. This is both reading
    and writing, so rate is 30hz. """
    def __init__(self):
        rospy.init_node('stepper_node', anonymous=False, log_level=rospy.INFO)
        self.stepper_cmd_sub = rospy.Subscriber('Stepper_Cmd', String, self.stepper_cmd_callback, queue_size=1, buff_size = 100)
        self.stepper_pos_pub = rospy.Publisher('Stepper_Pos',Int64, queue_size=1)
        self.upper_lim_switch_pub = rospy.Publisher('Upper_Lim_Switch_Status', Int32, queue_size=1)
        self.lower_lim_switch_pub = rospy.Publisher('Lower_Lim_Switch_Status', Int32, queue_size=1)

        self.pub_loop_rate = 40 # Hz
        self.pub_loop_rate_obj = rospy.Rate(self.pub_loop_rate)

        self.stepper = stepper.Stepper()

        rospy.on_shutdown(self.shutdown_function)
        self.pub_loop()

    def stepper_cmd_callback(self,msg):
        self.stepper.write(msg.data)

    def pub_loop(self):
        self.stepper.clean_before_read_start()
        while not rospy.is_shutdown():
            lower_switch_status,upper_switch_status,cur_pos,com_success = self.stepper.read()
            rospy.loginfo('{} {} {} {}'.format(lower_switch_status,upper_switch_status,cur_pos,com_success))
            if com_success:
                self.stepper_pos_pub.publish(int(cur_pos))
                self.upper_lim_switch_pub.publish(int(upper_switch_status))
                self.lower_lim_switch_pub.publish(int(lower_switch_status))
            self.pub_loop_rate_obj.sleep()

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        self.stepper.serial.close()

def main():
    _ = TestStandNode()

if __name__ == '__main__':
    main()
