#!/usr/bin/env python2

import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'support'))
import rospy
from std_msgs.msg import String,Float32,Int64,Int32,Bool
from contactile_gripper.msg import Float32List
import camera
import cv2
from collections import namedtuple

Pose = namedtuple("Pose", "pos ang")

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
            self.pose1_callback_counter, self.pose2_callback_counter, self.ten_vec_callback_counter= 0,0,0
            self.pred_pose1,self.pred_pose2, self.ten_vec = None,None,None
            self.update_pred_vars()
            self.pose_pred_sub1 = rospy.Subscriber('/Pose', Float32List, self.pose_pred_callback1, queue_size=1)
            self.pose_pred_sub2 = rospy.Subscriber('/Pose2', Float32List, self.pose_pred_callback2, queue_size=1)
            self.ten_vec_pred_sub = rospy.Subscriber('/tension_vec', Float32List, self.ten_vec_pred_callback, queue_size=1)
            self.good_grasp = False
            self.good_grasp_sub = rospy.Subscriber('/good_grasp', Bool, self.good_grasp_callback, queue_size=1)
        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 60
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.main_loop()

    def pose_pred_callback1(self, msg):
        self.pred_pose1 = Pose(msg.list[0], msg.list[1])
        self.pose1_callback_counter = 0

    def pose_pred_callback2(self,msg):
        self.pred_pose2 = Pose(msg.list[0],msg.list[1])
        self.pose2_callback_counter = 0

    def ten_vec_pred_callback(self,msg):
        self.ten_vec = Pose(msg.list[0],msg.list[1])
        self.ten_vec_callback_counter = 0

    def good_grasp_callback(self,msg): self.good_grasp = msg.data

    def update_pred_vars(self):
        """Keep track of the pose callbacks to know if there are no new poses."""
        self.pred_poses = []
        self.pose1_callback_counter += 1
        self.pose2_callback_counter += 1
        self.ten_vec_callback_counter += 1

    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            if self.mode == "ground_truth":
                success, ground_truth = self.cam.find_ground_truth(undistort=False, illustrations=True)
                cv2.imshow("Press q to exit.", self.cam.frame)
                self.cam_pub.publish([float(ground_truth.pos), float(ground_truth.ang)])
                print(ground_truth)
            if self.mode == "predict":
                ret = self.cam.cap_frame()
                if self.pose1_callback_counter < 10 and self.pred_pose1 is not None:
                    self.pred_poses.append(self.pred_pose1)
                if self.pose1_callback_counter < 10 and self.pred_pose2 is not None:
                    self.pred_poses.append(self.pred_pose2)
                if len(self.pred_poses) > 0 and self.ten_vec_callback_counter < 10:
                    success = self.cam.show_predictions(self.pred_poses,good_grasp=self.good_grasp,ten_vec = self.ten_vec, undistort=False)
                elif len(self.pred_poses) > 0:
                    success = self.cam.show_predictions(self.pred_poses,good_grasp=self.good_grasp, undistort=False)
                cv2.imshow("Press q to exit.", self.cam.frame)
                self.update_pred_vars()
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
            self.main_loop_rate_obj.sleep()

    def shutdown_function(self):
        cv2.destroyAllWindows()

def main():
    _ = CameraNode()

if __name__ == '__main__':
    main()