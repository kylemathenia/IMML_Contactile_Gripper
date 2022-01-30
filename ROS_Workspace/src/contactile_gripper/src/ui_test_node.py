#!/usr/bin/env python
"""
This is an example of the structure of a node that has multiple publishers publishing at different rates and a
subscriber. This examples does not function.
"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import sys, select, termios, tty, time
settings = termios.tcgetattr(sys.stdin)
def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist: key = sys.stdin.read(1)
    else: key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class ComplexNode(object):
    def __init__(self):
        self.publisher1 = rospy.Publisher('topic1',String, queue_size=10)
        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 1.0/10.0  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.main_loop()

    def main_loop(self):
        while not rospy.is_shutdown():
            key = getKey()
            if key == '\x7f': rospy.loginfo('back')
            elif key == ' ' or key == '\r' or key == '\x1b': rospy.loginfo('passive')
            elif key != '':
                rospy.loginfo(key)
                self.publisher1.publish(key)

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        pass

def main():
    rospy.init_node('complex_node_example',anonymous=False,log_level=rospy.DEBUG)
    complex_node = ComplexNode()

if __name__ == '__main__':
    main()
