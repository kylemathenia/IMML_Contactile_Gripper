#!/usr/bin/env python
"""
This is an example of the structure of a node that has multiple publishers publishing at different rates and a
subscriber. This examples does not function.
"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import gripper
import rosbag

class ComplexNode(object):
    def __init__(self):
        self.subscriber = rospy.Subscriber('Stepper_Cmd', String, self.callback, queue_size=1, buff_size=100)
        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 5  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.bag = rosbag.Bag('test.bag', 'w')
        rospy.on_shutdown(self.shutdown_function)
        self.main_loop()

    def callback(self,msg):
        rospy.loginfo('Callback executed.')
        self.bag.write('Stepper_Cmd', msg)
        # self.data = msg

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            rospy.loginfo('main_loop executed.')
            # self.publisher.publish(self.data)
            self.main_loop_rate_obj.sleep()

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        self.bag.close()

def main():
    rospy.init_node('complex_node_example',anonymous=False,log_level=rospy.DEBUG)
    complex_node = ComplexNode()

if __name__ == '__main__':
    main()
