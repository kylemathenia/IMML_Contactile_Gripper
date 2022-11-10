#!/usr/bin/env python2

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'support'))
import rospy
import time
import numpy as np
from contactile_gripper.msg import Float32List
from models import ModelType, DataOptions, PoseModel
from papillarray_ros_v2.msg import SensorState


# How to pass in arguments with launch file:
# https://campus-rover.gitbook.io/lab-notebook/faq/using-args-params-roslaunch
# https://www.folkstalk.com/2022/09/ros-launch-file-with-args-with-code-examples.html

# TODO. If not in contact, publish 999.

class PoseNode(object):
    """Takes 3 arguments: model type, data type, saved model path."""
    def __init__(self):
        rospy.init_node('pose_node', anonymous=False, log_level=rospy.INFO)
        # TODO make sure it finds the right folder.
        model_type, data_type, model_fn = self.sys.argv[0], sys.argv[1], sys.argv[2]
        # model_fn = "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/support/model_files/MLPRegressor_ALL.sav"
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

        self.main_loop_rate = 30  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.wait_for_data()
        self.main_loop()

    def get_pose_model(self, mt, dt, model_fn):
        if mt == ModelType.MLPRegressor.name: model_type = ModelType.MLPRegressor
        elif mt == ModelType.KNeighborsRegressor.name: model_type = ModelType.KNeighborsRegressor
        elif mt == ModelType.LinearAnalytical.name: model_type = ModelType.LinearAnalytical
        elif mt == ModelType.LinearRegression.name:model_type = ModelType.LinearRegression
        else: raise KeyError
        if dt == DataOptions.ALL.name: data_type = DataOptions.All
        elif dt == DataOptions.Z_ONLY.name: data_type = DataOptions.Z_ONLY
        elif dt == DataOptions.CONTACT_ONLY.name:data_type = DataOptions.CONTACT_ONLY
        else: raise KeyError
        return PoseModel(model_type, data_type=data_type, model_fn=model_fn)

    ######################## Subscriber and service callbacks ########################
    def tact_0_callback(self, msg):
        self.tact_sensor0 = msg
        self.in_contact_0 = msg.in_contact
        self.sensor0_pred_data = self.prep_sensor_data(msg)

    def tact_1_callback(self, msg):
        self.tact_sensor1 = msg
        self.in_contact_1 = msg.in_contact
        self.sensor1_pred_data = self.prep_sensor_data(msg)

    ######################## Main loop ########################
    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            pose = self.determine_pose()
            pose = self.pose_model.predict([self.tact_sensor0, self.tact_sensor1])
            if pose.position is None:
                self.pose_pub.publish([float(0), float(0)])
            else:
                self.pose_pub.publish([float(pose.position), float(pose.orientation)])
            self.main_loop_rate_obj.sleep()

    ######################## Functions ########################
    def determine_pose(self):
        if not self.in_contact_0 and not self.in_contact_0: return None
        poses = []
        poses.append(self.pose_model.model.predict(self.sensor0_pred_data))
        poses.append(self.pose_model.model.predict(self.sensor1_pred_data))



    def prep_sensor_data(self, d):
        """Get the data in the form the model expects for prediction."""
        prepped_data = []
        if self.pose_model.data_type == DataOptions.ALL:
            prepped_data += [d.gfX,d.gfY,d.gfZ]
        elif  self.pose_model.data_type == DataOptions.Z_ONLY:
            prepped_data += [d.gfZ]
        for pillar in d.pillars:
            if self.pose_model.data_type == DataOptions.ALL:
                prepped_data += [pillar.fX,pillar.fY,pillar.fZ,int(pillar.in_contact)]
            elif self.pose_model.data_type == DataOptions.Z_ONLY:
                prepped_data += [pillar.fZ]
            elif self.pose_model.data_type == DataOptions.CONTACT_ONLY:
                prepped_data += [int(pillar.in_contact)]
        print(prepped_data)
        return np.array([prepped_data])

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
