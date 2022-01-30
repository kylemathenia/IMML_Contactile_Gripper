#!/usr/bin/env python
"""
This is an example of the structure of a node that has multiple publishers publishing at different rates and a
subscriber. This examples does not function.
"""

import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from contactile_gripper.srv import *

class ControlNode(object):
    def __init__(self):
        self.goal_pos_publisher = rospy.Publisher('Goal_Position',Int32, queue_size=1)
        self.goal_cur_publisher = rospy.Publisher('Goal_Current', Int32, queue_size=1)
        self.motor_pos_subscriber = rospy.Subscriber('Motor_Position', Int32, self.motor_pos_callback, queue_size=1, buff_size=100)
        self.motor_pos_subscriber = rospy.Subscriber('UI_Mode', String, self.UI_mode_callback, queue_size=100, buff_size=10000)
        self.motor_pos_subscriber = rospy.Subscriber('UI_Input', String, self.UI_input_callback, queue_size=100, buff_size=1000)

        rospy.on_shutdown(self.shutdown_function)
        self.motor_command_loop_rate = 30  # Hz
        self.motor_command_loop_rate_obj = rospy.Rate(self.motor_command_loop_rate)

        self.UI_mode_options = set({'passive','position_control','sinusoidal_motion_routine'})
        self.UI_mode = 'passive'
        self.UI_mode = 'position_control'
        self.motor_pos = None
        self.motor_pos_set = False
        # Wait for motor_pos_subscriber to set motor_pos so goal_pos doesn't break the gripper trying to go to bad pos.
        while not self.motor_pos_set: rospy.logdebug('Waiting for motor position to be initialized...')
        self.goal_pos = self.motor_pos
        self.goal_cur = 0

        self.motor_command_loop()

    def motor_pos_callback(self,msg):
        """Read the encoder position of the motor."""
        rospy.logdebug('Motor position callback: {}'.format(msg.data))
        self.motor_pos = msg.data
        if not self.motor_pos_set: self.motor_pos_set = True  # Flag for node startup.

    def UI_mode_callback(self,msg):
        """Callback for when there is a change in user mode in the ui node."""
        try:
            assert msg.data in self.UI_mode_options
            if msg.data == 'passive': pass # service call was made directly in the ui_node to make passive.
            elif msg.data == 'position_control':
                self.goal_pos = self.motor_pos
                _ = self.change_mode_srv_client('position_control')
            self.UI_mode = msg.data
        except: rospy.logwarn('Cannot change UI mode. {} not in UI mode options: {}'.format(msg.data,self.UI_mode_options))

    def UI_input_callback(self,msg):
        """Callback for when the user inputs a command in the ui node."""
        if self.UI_mode == 'position_control':
            self.goal_pos = self.goal_pos + int(msg.data)

    def motor_command_loop(self):
        """Publishes motor commands to the motor depending on the current operating mode parameters."""
        while not rospy.is_shutdown():
            if self.UI_mode == 'passive':
                pass # Don't publish anything.
            elif self.UI_mode == 'position_control':
                self.goal_pos_publisher.publish(self.goal_pos)
            elif self.UI_mode == 'sinusoidal_motion_routine':
                # todo need to figure out how routines will be run from here.
                pass

            self.motor_command_loop_rate_obj.sleep()

    def change_mode_srv_client(self,mode):
        rospy.wait_for_service('change_mode_srv')
        try:
            change_mode_srv = rospy.ServiceProxy('change_mode_srv',ChangeMode)
            msg = change_mode_srv(mode)
            return msg.response
        except:
            rospy.logerr('Change mode service failed.')

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        pass

def main():
    rospy.init_node('complex_node_example',anonymous=False,log_level=rospy.DEBUG)
    _ = ControlNode()

if __name__ == '__main__':
    main()
