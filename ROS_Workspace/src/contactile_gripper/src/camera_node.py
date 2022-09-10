#!/usr/bin/env python2

import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'support'))
import rospy
from std_msgs.msg import String,Float32,Int64,Int32,Float32List
import camera
from pose_models import CameraGroundTruth

class CameraNode(object):
    """ROS node for the camera."""
    def __init__(self):
        rospy.init_node('camera_node', anonymous=False, log_level=rospy.INFO)
        self.cam = camera.Camera()
        self.cam_pub = rospy.Publisher('Ground_Truth_Pose', Float32List, queue_size=1)
        self.main_loop_rate = 300
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)

        self.cam.run()
        self.main_loop()

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            rospy.logdebug('In waiting: {}'.format(self.IMU.serial.in_waiting))
            ground_truth = self.cam.find_ground_truth()
            #Publish ground_truth.
            self.main_loop_rate_obj.sleep()

def main():
    _ = CameraNode()

if __name__ == '__main__':
    main()