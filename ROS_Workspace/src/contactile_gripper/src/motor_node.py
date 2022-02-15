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

#TODO: Add a pubplisher for gripper mode.
#TODO: Change the subscriber to handle commands of different types. Current and position.

class MotorNode(object):
    """ROS node for the Dynamixel motor. Max com speed is ~62hz for read or write operation. This is both reading
    and writing, so rate is 30hz. """
    def __init__(self):
        # Publishers
        self.gripper_pos_pub = rospy.Publisher('Gripper_Pos',Int64, queue_size=1)
        self.gripper_mode_pub = rospy.Publisher('Gripper_Mode',String, queue_size=1)

        self.pub_loop_rate = 10  # Hz
        self.pub_loop_rate_obj = rospy.Rate(self.pub_loop_rate)

        # Subscribers
        self.gripper_cmd_sub = rospy.Subscriber('Gripper_Cmd', Int64, self.gripper_cmd_callback, queue_size=1, buff_size = 100)

        # Services
        self.change_mode_srv = rospy.Service('change_mode_srv', ChangeMode, self.handle_change_mode)

        # Setup and start
        rospy.on_shutdown(self.shutdown_function)
        self.gripper = gripper.Gripper(fast_start=False)
        self.gripper.switch_modes('off')
        self.pub_loop()

    def handle_change_mode(self,req):
        if req.mode == 'passive':  # Use while loop to make sure it turns torque off.
            com_error = True
            while com_error:
                com_error = self.gripper.motor.write_torque_mode('off')
        elif req.mode == 'cur_based_pos_control':
            self.gripper.motor.switch_modes('cur_based_pos_control')
        else: rospy.logerr('Change mode service failed. "{}" is not a valid mode.'.format(req.mode))
        return ChangeModeResponse('Mode changed')

    def gripper_cmd_callback(self,msg):
        self.gripper.motor.write_goal_pos(msg.data)

    def pub_loop(self):
        """This is the main loop for the node which executes at self.pub_loop_rate."""
        while not rospy.is_shutdown():
            pos,err = self.gripper.motor.read_pos()
            if not err: self.motor_publisher.publish(pos)
            self.pub_loop_rate_obj.sleep()

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        pass

def main():
    rospy.init_node('motor_node', anonymous=False, log_level=rospy.INFO)
    gripper_node = MotorNode()

if __name__ == '__main__':
    main()
