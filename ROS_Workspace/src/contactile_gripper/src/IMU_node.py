#!/usr/bin/env python2
"""
This module contains the IMU node.
"""

import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'support'))
import rospy
from contactile_gripper.msg import Float32List
import IMU

class IMUNode(object):
    """ROS node for the IMU."""
    def __init__(self):
        rospy.init_node('IMU_node', anonymous=False, log_level=rospy.INFO)
        self.IMU = IMU.IMU()
        self.IMU_pub = rospy.Publisher('IMU_Acc', Float32List, queue_size=1)
        # Read rate must be faster than Arduino write rate to not have latency build-up in the communication buffer.
        # Arduino writes at roughly 280 hz on average.
        self.main_loop_rate = 300
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)

        self.IMU.clean_before_read_start()
        self.main_loop()

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            rospy.logdebug('In waiting: {}'.format(self.IMU.serial.in_waiting))
            x,y,z,com_success = self.IMU.read()
            if com_success:
                self.IMU_pub.publish([x,y,z])
            self.main_loop_rate_obj.sleep()

def main():
    _ = IMUNode()

if __name__ == '__main__':
    main()
