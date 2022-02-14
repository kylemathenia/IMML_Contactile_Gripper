#!/usr/bin/env python
"""
This is an example of the structure of a node that has multiple publishers publishing at different rates and a
subscriber. This examples does not function.
"""

import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from contactile_gripper.srv import *

class ControlNode(object):
    def __init__(self):
        self.goal_pos_publisher = rospy.Publisher('Stepper_Cmd',String, queue_size=1)

        self.motor_command_loop_rate = 0.2  # Hz
        self.motor_command_loop_rate_obj = rospy.Rate(self.motor_command_loop_rate)
        rospy.on_shutdown(self.shutdown_function)

        self.motor_command_loop()

    def motor_command_loop(self):
        """Publishes motor commands to the motor depending on the current operating mode parameters."""
        flag=True
        while not rospy.is_shutdown():
            if flag:
                cmd = "<s_500>"
                flag=False
            else:
                cmd = "<s_50>"
                flag=True
            print("Changed Command: {}".format(cmd))
            self.goal_pos_publisher.publish(cmd)
            self.motor_command_loop_rate_obj.sleep()

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        self.goal_pos_publisher.publish("x0")

def main():
    rospy.init_node('complex_node_example',anonymous=False,log_level=rospy.DEBUG)
    _ = ControlNode()

if __name__ == '__main__':
    main()
