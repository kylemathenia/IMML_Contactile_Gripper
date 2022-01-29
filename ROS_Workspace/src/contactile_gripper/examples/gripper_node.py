#!/usr/bin/env python
"""
This module contains the gripper node.
"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import gripper


class GripperNode(object):
    def __init__(self):
        self.subscriber1 = rospy.Subscriber('x', Float32, self.x_callback, queue_size=1, buff_size = 100)
        self.subscriber2 = rospy.Subscriber('y', Float32, self.y_callback, queue_size=1, buff_size=100)
        self.subscriber2 = rospy.Subscriber('y', Float32, self.z_callback, queue_size=1, buff_size=100)
        self.publisher1 = rospy.Publisher('topic1',Float32, queue_size=10)
        self.publisher2 = rospy.Publisher('topic2',Float32, queue_size=10)
        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 1.0/2.0 # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.pub2_freq = 0.1  # Hz
        rospy.Timer(rospy.Duration(1/self.pub2_freq), self.pub2_function)

        self.gripper = gripper.Gripper()
        self.data = None

        self.main_loop()

    def x_callback(self,msg):
        rospy.loginfo('x_callback executed.')
        # To make this data available to all of the methods in the class (for computing and publishing) set the message
        # to
        # self.data = msg

    def y_callback(self,msg):
        rospy.loginfo('y_callback executed.')
        # To make this data available to all of the methods in the class (for computing and publishing) set the message
        # to
        # self.data = msg

    def z_callback(self,msg):
        rospy.loginfo('z_callback executed.')
        # To make this data available to all of the methods in the class (for computing and publishing) set the message
        # to
        # self.data = msg

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            rospy.loginfo('publisher1 executed.')
            # self.publisher.publish(self.data)
            self.main_loop_rate_obj.sleep()

    def pub2_function(self,event=None):
        """This is a function that does something (publishes) at a different than the main loop. Rate controlled by
        the rospy.Timer() set in the __init__ function."""
        rospy.loginfo('publisher2 executed.')

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        pass

def main():
    rospy.init_node('motor_node',anonymous=False,log_level=rospy.DEBUG)
    gripper_node = GripperNode()

if __name__ == '__main__':
    main()
