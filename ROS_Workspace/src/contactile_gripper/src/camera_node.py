#!/usr/bin/env python2

import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'support'))
import rospy
from std_msgs.msg import String,Float32,Int64,Int32
from contactile_gripper.msg import Float32List
import camera
import cv2

class CameraNode(object):
    """ROS node for the camera."""
    def __init__(self):
        rospy.init_node('camera_node', anonymous=False, log_level=rospy.INFO)
        self.path_to_cal_images = r"/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/support/cal_images/"
        self.cam = camera.Camera(self.path_to_cal_images)
        self.cam_pub = rospy.Publisher('Ground_Truth_Pose', Float32List, queue_size=1)
        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 60
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.main_loop()

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            # rospy.logdebug('In waiting: {}'.format(self.IMU.serial.in_waiting))
            success, ground_truth = self.cam.find_ground_truth(undistort=False, illustrations=True)
            cv2.imshow("Press q to exit.", self.cam.frame)
            print(ground_truth)
            # if success:
            self.cam_pub.publish([float(ground_truth.position), float(ground_truth.orientation)])
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
            self.main_loop_rate_obj.sleep()

    def shutdown_function(self):
        cv2.destroyAllWindows()

def main():
    _ = CameraNode()

if __name__ == '__main__':
    main()