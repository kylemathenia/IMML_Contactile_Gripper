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
        possible_modes = {'ground_truth',"predict","normal"}
        # self.mode = sys.argv[0]
        self.mode = "predict"
        # self.mode = 'ground_truth'
        assert self.mode in possible_modes
        if self.mode == "ground_truth":
            self.cam_pub = rospy.Publisher('Ground_Truth_Pose', Float32List, queue_size=1)
        if self.mode == "predict":
            self.pose_pred_sub = rospy.Subscriber('/Pose', Float32List, self.pose_pred_callback, queue_size=1)
            self.pred_pose = None
        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 60
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.main_loop()

    def pose_pred_callback(self,msg):
        self.pred_pose = msg.list

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            if self.mode == "ground_truth":
                success, ground_truth = self.cam.find_ground_truth(undistort=False, illustrations=True)
                cv2.imshow("Press q to exit.", self.cam.frame)
                self.cam_pub.publish([float(ground_truth.pos), float(ground_truth.ang)])
                # print(ground_truth)
            if self.mode == "predict" and self.pred_pose is not None:
                success = self.cam.show_predictions(self.pred_pose, undistort=False)
                cv2.imshow("Press q to exit.", self.cam.frame)
                # print(success)
                # if success: cv2.imshow("Press q to exit.", self.cam.frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
            self.main_loop_rate_obj.sleep()

    def shutdown_function(self):
        cv2.destroyAllWindows()

def main():
    _ = CameraNode()

if __name__ == '__main__':
    main()