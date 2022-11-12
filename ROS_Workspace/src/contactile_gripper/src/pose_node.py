#!/usr/bin/env python2

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'support'))
import rospy
import time
import numpy as np
from contactile_gripper.msg import Float32List
from models import PoseModel
from papillarray_ros_v2.msg import SensorState
from collections import namedtuple
from enum import Enum


from models import ModelType, DataOptions
# class ModelType(Enum):
#     MLPRegressor = 1
#     KNeighborsRegressor = 2
#     LinearRegression = 3
#     LinearAnalytical = 4
#
# class DataOptions(Enum):
#     """The numbers are the number of input features for the data option."""
#     ALL = 39
#     Z_ONLY = 10
#     CONTACT_ONLY = 9

# How to pass in arguments with launch file:
# https://campus-rover.gitbook.io/lab-notebook/faq/using-args-params-roslaunch
# https://www.folkstalk.com/2022/09/ros-launch-file-with-args-with-code-examples.html

Pose = namedtuple("Pose", "pos ang")

class PoseNode(object):
    """Takes 3 arguments: model type, data type, saved model path. If not in contact, publish 999"""
    def __init__(self):
        rospy.init_node('pose_node', anonymous=False, log_level=rospy.INFO)
        # TODO make sure it finds the right folder.
        # model_type, data_type, model_fn = sys.argv[0], sys.argv[1], sys.argv[2]
        model_type, data_type = ModelType.KNeighborsRegressor.name, DataOptions.ALL.name
        fn = "/cable_pose_3_cable_with_forces_model_files/KNeighborsRegressor_ALL.sav"
        model_fn = "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/support/model_files/" + fn
        self.pose_model = self.get_pose_model(model_type, data_type, model_fn)
        # Publishers
        self.pose_pub = rospy.Publisher('Pose', Float32List, queue_size=1)
        # Subscribers
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_0', SensorState, self.tact_0_callback, queue_size=1)
        self.tact_sensor0 = None
        self.in_contact_1 = False
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_1', SensorState, self.tact_1_callback, queue_size=1)
        self.tact_sensor1 = None
        self.in_contact_1 = False

        self.main_loop_rate = 100  # Hz.
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.wait_for_data()
        self.main_loop()

    ######################## Subscriber and service callbacks ########################
    def tact_0_callback(self, msg):
        self.tact_sensor0 = msg
        self.in_contact_0 = msg.is_contact
        self.sensor0_pred_data = self.prep_sensor_data(msg)

    def tact_1_callback(self, msg):
        self.tact_sensor1 = msg
        self.in_contact_1 = msg.is_contact
        self.sensor1_pred_data = self.prep_sensor_data(msg)

    ######################## Main loop ########################
    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            # if not self.in_contact_0 or not self.in_contact_1:
            #     self.pose_pub.publish([float(999), float(999)])
            pose = self.determine_pose()
            if self.in_contact_0 and self.in_contact_1:
                self.pose_pub.publish([float(pose.pos), float(pose.ang)])
            self.main_loop_rate_obj.sleep()

    ######################## Other ########################
    def determine_pose(self):
        if not self.in_contact_0 and not self.in_contact_0: return Pose(999, 999)
        pred0 = self.pose_model.model.predict(self.sensor0_pred_data)
        pred1 = self.pose_model.model.predict(self.sensor1_pred_data)
        # Flip sensor 1's angle prediction because on the gripper it is mirrored.
        pred0[0][1] = -pred0[0][1]
        pose = np.average([pred0[0],pred1[0]],axis=0)
        return Pose(pose[0], pose[1])
        # return Pose(pred1[0][0],pred1[0][1])


    def prep_sensor_data(self, d):
        """Get the data in the form the model expects for prediction."""
        prepped_data = []
        if self.pose_model.data_type == DataOptions.ALL:
            prepped_data += [d.gfX,d.gfY,d.gfZ]
            # print("gfX: {}, gfY: {}, gfZ: {}".format(d.gfX,d.gfY,d.gfZ))
        elif  self.pose_model.data_type == DataOptions.Z_ONLY:
            prepped_data += [d.gfZ]
        for pillar in d.pillars:
            if self.pose_model.data_type == DataOptions.ALL:
                # print("fX: {}, fY: {}, fZ: {}, contact: {}".format(pillar.fX,pillar.fY,pillar.fZ,int(pillar.in_contact)))
                prepped_data += [pillar.fX,pillar.fY,pillar.fZ,int(pillar.in_contact)]
            elif self.pose_model.data_type == DataOptions.Z_ONLY:
                prepped_data += [pillar.fZ]
            elif self.pose_model.data_type == DataOptions.CONTACT_ONLY:
                prepped_data += [int(pillar.in_contact)]
        return np.array([prepped_data])

    def get_pose_model(self, mt, dt, model_fn):
        if mt == ModelType.MLPRegressor.name: model_type = ModelType.MLPRegressor
        elif mt == ModelType.KNeighborsRegressor.name: model_type = ModelType.KNeighborsRegressor
        elif mt == ModelType.LinearAnalytical.name: model_type = ModelType.LinearAnalytical
        elif mt == ModelType.LinearRegression.name:model_type = ModelType.LinearRegression
        else: raise KeyError
        if dt == DataOptions.ALL.name: data_type = DataOptions.ALL
        elif dt == DataOptions.Z_ONLY.name: data_type = DataOptions.Z_ONLY
        elif dt == DataOptions.CONTACT_ONLY.name:data_type = DataOptions.CONTACT_ONLY
        else: raise KeyError
        return PoseModel(model_type, data_type=data_type, model_fn=model_fn)

    def wait_for_data(self):
        while True:
            if self.tact_sensor0 is not None and self.tact_sensor1 is not None:
                return
            rospy.loginfo("PoseNode is waiting for tactile sensor data.")
            time.sleep(.5)


def main():
    _ = PoseNode()


if __name__ == '__main__':
    main()
