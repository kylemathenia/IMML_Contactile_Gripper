#!/usr/bin/env python
"""
This module contains the gripper node.
"""

import roslib; roslib.load_manifest('contactile_gripper')
from contactile_gripper.srv import *
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Int64
import gripper

class GripperNode(object):
    """ROS node for the gripper. Max com speed is ~62hz for read or write operation. This is both reading
    and writing, so rate is 30hz. """
    def __init__(self):
        # Initialize and calibrate gripper.
        self.gripper = gripper.Gripper(fast_start=False)

        # Publishers
        self.gripper_pos_pub = rospy.Publisher('Gripper_Pos',Int64, queue_size=1)
        self.gripper_mode_pub = rospy.Publisher('Gripper_Mode',String, queue_size=1)

        self.pub_loop_rate = 10  # Hz
        self.pub_loop_rate_obj = rospy.Rate(self.pub_loop_rate)

        # Subscribers
        self.gripper_cmd_sub = rospy.Subscriber('Gripper_Cmd', Int64, self.gripper_cmd_callback, queue_size=1, buff_size = 100)

        # Services
        self.gripper_change_mode_srv = rospy.Service('gripper_change_mode_srv', GripperChangeMode, self.srv_handle_change_mode)

        # Setup and start
        rospy.on_shutdown(self.shutdown_function)
        self.pub_loop()

    def pub_loop(self):
        """This is the main loop for the node which executes at self.pub_loop_rate."""
        while not rospy.is_shutdown():
            pos,com_err = self.gripper.motor.read_pos()
            if not com_err: self.motor_publisher.publish(pos)
            self.gripper_mode_pub(self.gripper.mode)
            self.pub_loop_rate_obj.sleep()

    def gripper_cmd_callback(self, msg):
        cmd = msg.data.split('_')
        cmd_mode = cmd[0]
        cmd_val = cmd[1]
        if cmd_mode == 'position':
            self.gripper.motor.write_goal_pos(cmd_val)
        elif cmd_mode == 'current':
            self.gripper.motor.write_goal_cur(cmd_val)

    def srv_handle_change_mode(self, req):
        if req.mode == 'passive':  # Use while loop to make sure it turns torque off.
            com_error = True
            while com_error:
                com_error = self.gripper.switch_modes('off')
        elif req.mode == 'cur_based_pos_control':
            com_error = self.gripper.switch_modes('cur_based_pos_control')
        else:
            rospy.logerr('Change mode service failed. "{}" is not a valid mode.'.format(req.mode))
        return GripperChangeModeResponse('Mode changed')

    def shutdown_function(self):
        com_error = self.gripper.switch_modes('off')

def main():
    rospy.init_node('gripper_node', anonymous=False, log_level=rospy.INFO)
    gripper_node = GripperNode()

if __name__ == '__main__':
    main()
