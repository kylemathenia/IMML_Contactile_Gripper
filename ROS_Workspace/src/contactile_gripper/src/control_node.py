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

class ControlNode(object):
    def __init__(self):
        self.goal_pos_publisher = rospy.Publisher('Goal_Position',Int32, queue_size=1)
        self.goal_cur_publisher = rospy.Publisher('Goal_Current', Int32, queue_size=1)
        self.motor_pos_subscriber = rospy.Subscriber('Motor_Position', Int32, self.motor_pos_callback, queue_size=1, buff_size=100)
        self.motor_pos_subscriber = rospy.Subscriber('UI_Mode', String, self.UI_mode_callback, queue_size=100, buff_size=10000)
        self.motor_pos_subscriber = rospy.Subscriber('UI_Input', String, self.UI_input_callback, queue_size=100, buff_size=10000)
        rospy.on_shutdown(self.shutdown_function)
        self.motor_command_loop_rate = 30  # Hz
        self.motor_command_loop_rate_obj = rospy.Rate(self.motor_command_loop_rate)
        self.pub2_freq = 0.2  # Hz
        rospy.Timer(rospy.Duration(1/self.pub2_freq), self.pub2_function)

        self.UI_mode_options = set({'passive','position_control','sinusoidal_motion_routine'})
        self.UI_mode = 'passive'
        self.UI_mode = 'direct_control'
        self.motor_pub_mode = 'current'
        self.motor_pos = None
        self.motor_pos_set = False
        # Wait for motor_pos_subscriber to set motor_pos so goal_pos doesn't break the gripper trying to go to bad pos.
        while not self.motor_pos_set: rospy.logdebug('Waiting for motor position to be initialized...')
        self.goal_pos = self.motor_pos
        self.goal_cur = 0

        self.motor_command_loop()

    def motor_pos_callback(self,msg):
        self.motor_pos = msg.data
        if not self.motor_pos_set: self.motor_pos_set = True  # Flag for node startup.

    def UI_mode_callback(self,msg):
        try:
            assert msg.data in self.UI_mode_options
            self.UI_mode = msg.data
        except: rospy.logwarn('Cannot change UI mode. {} not in UI mode options: {}'.format(msg.data,self.UI_mode_options))

    def UI_input_callback(self,msg):
        if UI_mode = 'direct_control' and msg.data = 'e':
            self.goal_pos = self.goal_pos + 5

    def motor_command_loop(self):
        """Publishes motor commands to the motor depending on the current operating mode parameters."""
        while not rospy.is_shutdown():
            if self.UI_mode == 'passive':
                pass # Don't publish anything.
            elif self.UI_mode == 'position_control' and self.motor_pub_mode == 'position':
                self.goal_pos_publisher.publish(self.goal_pos)
            elif self.UI_mode == 'sinusoidal_motion_routine':
                pass

            self.motor_command_loop_rate_obj.sleep()

    def pub2_function(self,event=None):
        """This is a function that does something (publishes) at a different than the main loop. Rate controlled by
        the rospy.Timer() set in the __init__ function."""
        # rospy.loginfo('pub2_function executed.')
        pass

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        pass

def main():
    rospy.init_node('complex_node_example',anonymous=False,log_level=rospy.DEBUG)
    _ = ControlNode()

if __name__ == '__main__':
    main()
