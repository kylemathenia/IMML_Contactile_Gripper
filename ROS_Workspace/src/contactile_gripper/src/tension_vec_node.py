#!/usr/bin/env python2

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'support'))
import rospy
import time
import numpy as np
from contactile_gripper.msg import Float32List
from models import TensionVecModel
from std_msgs.msg import Bool
from papillarray_ros_v2.msg import SensorState
from collections import namedtuple
from enum import Enum

from models import ModelType

TensionVec = namedtuple("TensionVec", "roll pitch")

class TensionVecNode(object):
    """Takes 3 arguments: model type, saved model path. If pose is not good, does not publish tension vec prediction."""
    def __init__(self):
        rospy.init_node('tension_vec_node', anonymous=False, log_level=rospy.INFO)
        # TODO make sure it finds the right folder.
        # model_type, data_type, model_fn = sys.argv[0], sys.argv[1], sys.argv[2]
        model_type = ModelType.KNeighborsRegressor.name
        fn = "/cable_tension_vec_model_files/KNeighborsRegressor_5neighbors.sav"
        # model_type= ModelType.MLPRegressor.name
        # fn = "/cable_tension_vec_model_files/MLPRegressor_0.sav"
        model_fn = "/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/support/model_files/" + fn
        self.ten_vec_model = self.get_ten_vec_model(model_type, model_fn)
        # Publishers
        self.tension_vec_pub = rospy.Publisher('tension_vec', Float32List, queue_size=1)
        # Subscribers
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_0', SensorState, self.tact_0_callback, queue_size=1)
        self.tact_sensor0 = None
        self.in_contact_1 = False
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_1', SensorState, self.tact_1_callback, queue_size=1)
        self.tact_sensor1 = None
        self.in_contact_1 = False
        self.good_grasp_sub = rospy.Subscriber('/good_grasp', Bool, self.good_grasp_callback, queue_size=1)
        self.good_grasp = False

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

    def good_grasp_callback(self,msg):
        self.good_grasp = msg.data

    ######################## Main loop ########################
    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            tension_vec = self.determine_tension_vec()
            if self.good_grasp:
                self.tension_vec_pub.publish([float(tension_vec.roll), float(tension_vec.pitch)])
            self.main_loop_rate_obj.sleep()

    ######################## Other ########################
    def determine_tension_vec(self):
        if not self.good_grasp: return TensionVec(999, 999)
        self.sensor_pred_data = np.array([np.append(self.sensor0_pred_data, self.sensor1_pred_data)])
        pred = self.ten_vec_model.model.predict(self.sensor_pred_data)
        return TensionVec(pred[0][0], pred[0][1])

    def prep_sensor_data(self, d):
        """Get the data in the form the model expects for prediction."""
        prepped_data = []
        prepped_data += [d.gfX,d.gfY,d.gfZ]
        for pillar in d.pillars:
            prepped_data += [pillar.fX,pillar.fY,pillar.fZ,pillar.dX,pillar.dY,pillar.dZ,int(pillar.in_contact)]
        return np.array([prepped_data])

    def get_ten_vec_model(self, mt, model_fn):
        if mt == ModelType.MLPRegressor.name: model_type = ModelType.MLPRegressor
        elif mt == ModelType.KNeighborsRegressor.name: model_type = ModelType.KNeighborsRegressor
        elif mt == ModelType.LinearRegression.name:model_type = ModelType.LinearRegression
        else: raise KeyError
        return TensionVecModel(model_type, model_fn=model_fn)

    def wait_for_data(self):
        while True:
            if self.tact_sensor0 is not None and self.tact_sensor1 is not None:
                return
            rospy.loginfo("PoseNode is waiting for tactile sensor data.")
            time.sleep(.5)


def main():
    _ = TensionVecNode()


if __name__ == '__main__':
    main()
