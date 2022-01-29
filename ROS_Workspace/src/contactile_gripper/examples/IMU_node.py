#!/usr/bin/env python
"""
This module contains the IMU node.
"""

import rospy
from std_msgs.msg import Float32
import IMU

class IMUNode(object):
    """ROS node for the IMU."""
    def __init__(self):
        self.IMU = IMU.IMU()
        self.pubx = rospy.Publisher('x', Float32, queue_size=1)
        self.puby = rospy.Publisher('y', Float32, queue_size=1)
        self.pubz = rospy.Publisher('z', Float32, queue_size=1)
        self.main_loop_rate = 1.0/5.0
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.x = None
        self.y = None
        self.z = None

        self.IMU.clean_before_read_start()
        self.main_loop()

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            x,y,z,com_success = self.IMU.read()
            if com_success:
                self.pubx.publish(x)
                self.puby.publish(y)
                self.pubz.publish(z)
            self.main_loop_rate_obj.sleep()

def main():
    rospy.init_node('IMU_node',anonymous=False,log_level=rospy.DEBUG)
    IMU_node = IMUNode()

if __name__ == '__main__':
    main()
