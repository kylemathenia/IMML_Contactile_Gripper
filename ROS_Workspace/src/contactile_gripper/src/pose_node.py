#!/usr/bin/env python2

import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'support'))
import rospy
import time
from contactile_gripper.msg import Float32List
from pose_models import LinearAnalytical
from papillarray_ros_v2.msg import SensorState

class PoseNode(object):
    def __init__(self):
        rospy.init_node('pose_node', anonymous=False, log_level=rospy.INFO)
        self.pose_model = LinearAnalytical()
        # Publishers
        self.pose_pub = rospy.Publisher('Pose', Float32List, queue_size=1)
        #Subscribers
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_0', SensorState, self.tact_0_callback, queue_size=1)
        self.tact_sensor0 = None
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_1', SensorState, self.tact_1_callback, queue_size=1)
        self.tact_sensor1 = None

        self.main_loop_rate = 30  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.wait_for_data()
        self.main_loop()

    ######################## Subscriber and service callbacks ########################
    def tact_0_callback(self,msg):
        self.tact_sensor0 = msg
    def tact_1_callback(self,msg):
        self.tact_sensor1 = msg

    ######################## Main loop ########################
    def main_loop(self):
        """This is the main loop for the node which executes at self.main_loop_rate."""
        while not rospy.is_shutdown():
            pose = self.pose_model.predict([self.tact_sensor0,self.tact_sensor1])
            if pose.position is None:
                self.pose_pub.publish([float(0), float(0)])
            else:
                self.pose_pub.publish([float(pose.position),float(pose.orientation)])
            self.main_loop_rate_obj.sleep()

    ######################## Functions ########################
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
