#!/usr/bin/env python
"""
This module contains the IMU node.
"""

import time
import rospy
from std_msgs.msg import String,Float32,Int64,Int32,Bool
from papillarray_ros_v2.msg import SensorState
from contactile_gripper.msg import Float32List,Int32List
from contactile_gripper.srv import *
import srv_clients

class TESTNode(object):
    """ROS node for the IMU."""
    def __init__(self):
        rospy.init_node('test_node', anonymous=False, log_level=rospy.DEBUG)
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_0', SensorState, self.tact_0_callback, queue_size=1)
        self.tact_sensor0 = None

    def tact_0_callback(self,msg):
        self.tact_sensor0 = msg
        print("Global z force: {}".format(msg.gfZ))

def main():
    _ = TESTNode()
    rospy.spin()

if __name__ == '__main__':
    main()
