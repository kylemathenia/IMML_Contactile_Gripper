#!/usr/bin/env python
"""
This is an example of the structure of a node that has multiple publishers publishing at different rates and a
subscriber. This examples does not function.
"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import gripper

class ComplexNode(object):
    def __init__(self):
        self.publisher1 = rospy.Publisher('topic1',Int64, queue_size=10)
        self.publisher2 = rospy.Publisher('topic2'.format(multiplier), Int64, queue_size=10)
        self.subscriber = rospy.Subscriber('topic3', Float32, self.callback, queue_size=1, buff_size=100)
        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 5  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.pub2_freq = 0.2  # Hz
        rospy.Timer(rospy.Duration(1/self.pub2_freq), self.pub2_function)

        self.data = None

        self.main_loop()

    def callback(self,msg):
        rospy.loginfo('Callback executed.')
        # To make this data available to all of the methods in the class (for computing and publishing) set the message
        # to
        # self.data = msg

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            rospy.loginfo('main_loop executed.')
            # self.publisher.publish(self.data)
            self.main_loop_rate_obj.sleep()

    def pub2_function(self,event=None):
        """This is a function that does something (publishes) at a different than the main loop. Rate controlled by
        the rospy.Timer() set in the __init__ function."""
        rospy.loginfo('pub2_function executed.')

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        pass

def main():
    rospy.init_node('complex_node_example',anonymous=False,log_level=rospy.DEBUG)
    complex_node = ComplexNode()
    # rospy.spin() is not needed because there is an infinite main loop to keep everything alive.

if __name__ == '__main__':
    main()
