#!/usr/bin/env python2
"""
This module contains a node to test the system hardware, and publish a message if everything is good. Takes in
command line arguments for the configuration of the system.
"""

#TODO Implement a test node. Command line arguments are passed to the script. These are created in the launch.py file.

import sys,os
import rospy
from contactile_gripper.msg import Float32List

class TestNode(object):
    """Test hardware and publish a message if everything looks good."""
    def __init__(self):
        rospy.init_node('sys_test_node', anonymous=False, log_level=rospy.INFO)
        self.config = sys.argv
        if "camera" in self.config:
            pass
        if "IMU" in self.config:
            pass
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
